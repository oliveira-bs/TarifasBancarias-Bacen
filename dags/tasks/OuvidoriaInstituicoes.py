import json

import requests
from tasks.SaveJSON_CSV import SaveCSVFile


def _extract_ouvidoriainstituicoes(**kwargs):
    HEADER_FILE = open(kwargs['header_file'])
    HEADERS = json.load(HEADER_FILE)

    url = HEADERS['ouvidoria']['url']
    payload = HEADERS['ouvidoria']['payload']
    headers = HEADERS['ouvidoria']['headers']

    pathfolder = kwargs['pathfolder_tables']
    name_csv = 'OuvidoriaInstituicoes.csv'

    def Request_OuvidoriaInstituicoes(url: str, headers: dict, payload: dict):
        response = requests.request("GET", url, headers=headers, data=payload)
        data_request = json.loads(response.text)
        return data_request['value']

    SaveCSVFile(filename=name_csv,
                data_request=Request_OuvidoriaInstituicoes(url, headers,
                                                           payload),
                pathfolder=pathfolder)

    return
