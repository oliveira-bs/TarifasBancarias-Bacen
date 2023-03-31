
def ArgsThreadTarifas(url: str, cnpjs: list,
                      service_option: dict) -> list:
    args = []
    for index_file, cnpj in enumerate(cnpjs):
        for option in service_option.values():
            url_base = url.split('_%variable#item%_')
            url_cnpj = ''.join(
                [url_base[0], option, url_base[1], cnpj, url_base[2]])

            args.append((url_cnpj, index_file, option, cnpj))

    return args
