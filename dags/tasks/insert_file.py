import psycopg2 as ps


def insert_csv(**kwargs):
    conn = ps.connect(host='host.docker.internal',
                      user='airflow',
                      password='airflow',
                      database='airflow-db',
                      port=5433,
                      options=f"-c search_path={kwargs['schema']}")

    cur = conn.cursor()

    with open(kwargs['path'], 'r') as f:
        # Skip the header row.
        next(f)
        cur.copy_from(f, kwargs['table_name'], sep=kwargs['sep'])

    conn.commit()
