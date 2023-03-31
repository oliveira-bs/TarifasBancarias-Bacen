from os import path, remove


def ExcludeFile(pathfolder: str, name_csv: str):
    if path.exists(f'{pathfolder}/{name_csv}'):
        remove(f'{pathfolder}/{name_csv}')
