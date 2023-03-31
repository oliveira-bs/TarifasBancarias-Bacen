import csv


def ExtractVar(pathfolder: str, filename_csv_extract: str,
               index_column: int = 0):
    complete_filename = f'{pathfolder}/{filename_csv_extract}'

    cods = []
    try:
        with open(complete_filename, 'r') as f:
            next(f)
            reader_obj = csv.reader(f, delimiter='|')
            for row in reader_obj:
                cods.append(row[index_column])
        return cods
    except ValueError as ValErr:
        raise ValueError(ValErr)
    except FileExistsError or FileNotFoundError:
        print(f"Problema com o arquivo {complete_filename}")
        return
