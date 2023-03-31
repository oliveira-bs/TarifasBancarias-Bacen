import json

import requests

from tasks.ExcluedFileExists import ExcludeFile
from tasks.ExtractArgsThread import ArgsThreadTarifas
from tasks.ExtractVarTable import ExtractVar
from tasks.SaveJSON_CSV import SaveCSVFileLoop
from tasks.ThreadProcess import Thread


def _extract_listatarifas(**kwargs):
    HEADER_FILE = open(kwargs['header_file'])
    HEADERS = json.load(HEADER_FILE)

    url = HEADERS['tarifas']['url']
    payload = HEADERS['tarifas']['payload']
    headers = HEADERS['tarifas']['headers']

    pathfolder = kwargs['pathfolder_tables']
    filename_csv_extract = 'ListaInstituicoes.csv'
    name_csv = 'ListaTarifas.csv'

    cnpjs = ExtractVar(pathfolder, filename_csv_extract, index_column=0)
    service_option = {'pessoa_juridica': 'J', 'pessoa_fisica': 'F'}

    ExcludeFile(pathfolder, name_csv)

    def Request_Tarifas(url: str, headers: dict, payload: dict,
                        cnpj: str = None, columnnamecod: str = 'Codigo'):

        response = requests.request(
            "GET", url, headers=headers, data=payload)
        data_request = json.loads(response.text)
        data_request = data_request['value']
        for item in data_request:
            item.update({f'{columnnamecod}': cnpj})

        return data_request

    def Request_Save(url, index_file, option_choice, cnpj):
        SaveCSVFileLoop(filename=name_csv,
                        data_request=Request_Tarifas(url=url, headers=headers,
                                                     payload=payload,
                                                     cnpj=cnpj,
                                                     columnnamecod='CNPJ'),
                        pathfolder=pathfolder,
                        modewrite='a')
        return

    args = ArgsThreadTarifas(
        url=url, cnpjs=cnpjs, service_option=service_option)

    Thread(function_thread=Request_Save, args_thread=args, max_workers=8)

    return 'ThreadProcess - Finished'
