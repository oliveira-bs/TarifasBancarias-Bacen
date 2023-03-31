import json

import requests
from tasks.ExcluedFileExists import ExcludeFile
from tasks.ExtractVarTable import ExtractVar
from tasks.SaveJSON_CSV import SaveCSVFileLoop


def _extract_listainstituicoes(**kwargs):
    HEADER_FILE = open(kwargs['header_file'])
    HEADERS = json.load(HEADER_FILE)

    url = HEADERS['instituicoes']['url']
    payload = HEADERS['instituicoes']['payload']
    headers = HEADERS['instituicoes']['headers']

    pathfolder = kwargs['pathfolder_tables']
    filename_csv_extract = 'GruposConsolidados.csv'
    name_csv = 'ListaInstituicoes.csv'

    cods = ExtractVar(pathfolder, filename_csv_extract)

    ExcludeFile(pathfolder, name_csv)

    def Request_ListaInstituicoes(url: str = None, headers: dict = headers,
                                  payload: dict = payload, cod: str = None,
                                  columnnamecod: str = 'Codigo'):
        url_base = url.split('_%variable#item%_')
        url_cod = ''.join([url_base[0], cod, url_base[1]])
        response = requests.request(
            "GET", url_cod, headers=headers, data=payload)
        data_request = json.loads(response.text)
        data_request = data_request['value']
        for item in data_request:
            item.update({f'{columnnamecod}': cod})
        return data_request

    for index_file, cod in enumerate(cods):
        SaveCSVFileLoop(filename=name_csv,
                        data_request=Request_ListaInstituicoes(
                            url, headers, payload, cod,
                            columnnamecod='Codigo'),
                        pathfolder=pathfolder,
                        modewrite='a')
    return
