import numpy


class ObjectSet:

    def __init__(self, connectivity: int) -> None: ...

    def num_objects(self) -> int: ...

    def add_tile(
        self,
        tile: numpy.ndarray[numpy.dtype[numpy.bool_]],
        start: tuple[int, int, int],
        stop: tuple[int, int, int],
    ) -> None: ...

    def digest(self) -> int: ...

    def extract_tile(
        self,
        tile: numpy.ndarray[numpy.dtype[numpy.uintc]],
        start: tuple[int, int, int],
        stop: tuple[int, int, int],
    ) -> None: ...
