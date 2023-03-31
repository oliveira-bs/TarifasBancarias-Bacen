import json

import requests
from tasks.SaveJSON_CSV import SaveCSVFile


def _extract_gruposconsolidados(**kwargs):

    HEADER_FILE = open(kwargs['header_file'])
    HEADERS = json.load(HEADER_FILE)

    url = HEADERS['grupos']['url']
    payload = HEADERS['grupos']['payload']
    headers = HEADERS['grupos']['headers']

    pathfolder = kwargs['pathfolder_tables']
    name_csv = 'GruposConsolidados.csv'

    def Request_GruposConsolidados(url: str, headers: dict, payload: dict):
        response = requests.request("GET", url, headers=headers, data=payload)
        data_request = json.loads(response.text)
        return data_request['value']

    SaveCSVFile(filename=name_csv,
                data_request=Request_GruposConsolidados(url, headers, payload),
                pathfolder=pathfolder)

    return
