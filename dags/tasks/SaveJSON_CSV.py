import csv
import os
from os import getcwd, mkdir, path


def SaveCSVFileLoop(filename: str, data_request: list,
                    pathfolder: str = getcwd(), modewrite: str = 'w'
                    ):
    data = data_request
    if not len(data) == 0:
        csv_headers = data[0].keys()
        if not path.exists(pathfolder):
            mkdir(pathfolder)

        complete_filename = f'{pathfolder}/{filename}'
        file_exists = os.access(complete_filename, os.F_OK)

        with open(complete_filename, modewrite, encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers, delimiter='|')
            if not file_exists:
                writer.writeheader()
            writer.writerows(data)
    return


def SaveCSVFile(filename: str, data_request: list, pathfolder: str = getcwd(),
                modewrite: str = 'w'):
    data = data_request
    if not len(data) == 0:
        csv_headers = data[0].keys()
        if not path.exists(pathfolder):
            mkdir(pathfolder)

        complete_filename = f'{pathfolder}/{filename}'
        with open(complete_filename, modewrite, encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers, delimiter='|')
            writer.writeheader()
            writer.writerows(data)
    return
