from concurrent.futures import ThreadPoolExecutor


def Thread(function_thread, args_thread: list,
           max_workers: int | None = 4) -> None:
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(function_thread, *zip(*args_thread))
    return
