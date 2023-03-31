from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.task_group import TaskGroup
from tasks.GruposConsolidados import _extract_gruposconsolidados
from tasks.insert_file import insert_csv
from tasks.ListaInstituicoes import _extract_listainstituicoes
from tasks.ListaTarifasThread import _extract_listatarifas
from tasks.OuvidoriaInstituicoes import _extract_ouvidoriainstituicoes

# ------------------ GLOBAL VARIABLES ---------------------

HEADER_FILE = "/opt/airflow/dags/utils/headers_requests.json"
PATHFOLDER_TABLES = '/opt/airflow/raw/tables/tarifasbancarias'
INFOS_TASKS_INSERT = [{"id": "grupos", "filename": "GruposConsolidados.csv"},
                      {"id": "instituicoes",
                       "filename": "ListaInstituicoes.csv"},
                      {"id": "tarifas", "filename": "ListaTarifas.csv"},
                      {"id": "ouvidorias",
                       "filename": "OuvidoriaInstituicoes.csv"}]

# ------------------- DAG DEFINITION ----------------------

with DAG(
    dag_id="etl_tarifasbancarias_bcb",
    start_date=pendulum.datetime(2023, 1, 1, tz="America/Sao_Paulo"),
    catchup=False,
    schedule=None,
    max_active_runs=1,
    concurrency=1,
    template_searchpath='/opt/airflow/sql',
    default_args={'owner': 'oliveira.bs',
                  'retry_delay': timedelta(seconds=5),
                  'retries': 1,
                  'email_on_failure': False,
                  },
    tags=["Data ingestion", "API", "Tarifas Bancarias",
          "Instituiçoes Financeiras"],
) as dag:

    extract_gruposconsolidados = PythonOperator(
        task_id='extract_gruposconsolidados',
        python_callable=_extract_gruposconsolidados,
        op_kwargs={"header_file": HEADER_FILE,
                   "pathfolder_tables": PATHFOLDER_TABLES},
        dag=dag,
    )

    extract_listainstituicoes = PythonOperator(
        task_id='extract_listainstituicoes',
        python_callable=_extract_listainstituicoes,
        op_kwargs={"header_file": HEADER_FILE,
                   "pathfolder_tables": PATHFOLDER_TABLES},
        dag=dag,
    )

    extract_listatarifas = PythonOperator(
        task_id='extract_listatarifas',
        python_callable=_extract_listatarifas,
        op_kwargs={"header_file": HEADER_FILE,
                   "pathfolder_tables": PATHFOLDER_TABLES},
        dag=dag,
    )

    extract_ouvidoriainstituicoes = PythonOperator(
        task_id='extract_ouvidoriainstituicoes',
        python_callable=_extract_ouvidoriainstituicoes,
        op_kwargs={"header_file": HEADER_FILE,
                   "pathfolder_tables": PATHFOLDER_TABLES},
        dag=dag,
    )

    create_table = PostgresOperator(
        task_id='create_table_db',
        postgres_conn_id="postgres_airflow",
        sql='tarifasbancarias/createtables.sql'
    )

    truncate_tables = PostgresOperator(
        task_id='truncate_tables_db',
        postgres_conn_id="postgres_airflow",
        sql='tarifasbancarias/truncatetables.sql'
    )
    with TaskGroup("insert_data") as insert_data:
        task_insert = []
        for info in INFOS_TASKS_INSERT:
            insert = PythonOperator(
                task_id=f'table_{info.get("id")}',
                python_callable=insert_csv,
                op_kwargs={'path':
                           f'{PATHFOLDER_TABLES}/{info.get("filename")}',
                           'schema': 'tarifas',
                           'table_name': f'{info.get("id")}',
                           'sep': '|'},
                dag=dag,
            )
            task_insert.append(f'insert_{info.get("id")}')
        task_insert

    insertjoin_tarifas_instituicoes = PostgresOperator(
        task_id='insertjoin_tarifas_instituicoes_db',
        postgres_conn_id="postgres_airflow",
        sql='tarifasbancarias/insertjoin_tarifas_instituicoes.sql'
    )

    insertjoin_tarifas_ouvidorias = PostgresOperator(
        task_id='insertjoin_tarifas_ouvidorias_db',
        postgres_conn_id="postgres_airflow",
        sql='tarifasbancarias/insertjoin_tarifas_ouvidorias.sql'
    )

    extract_gruposconsolidados >> extract_listainstituicoes >> \
        extract_listatarifas >> create_table >> \
        [truncate_tables, extract_ouvidoriainstituicoes] >> \
        insert_data >> insertjoin_tarifas_instituicoes >> \
        insertjoin_tarifas_ouvidorias
