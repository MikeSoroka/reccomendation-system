from typing import Iterable, Sized


class DataUtils:
    @staticmethod
    def chunks(data: list, chunk_size: int = 10000) -> Iterable[Iterable]:
        for i in range(0, len(data), chunk_size):
            yield data[i : i + chunk_size]