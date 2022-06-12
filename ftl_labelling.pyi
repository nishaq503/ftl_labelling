import numpy

class PolygonSet:

    def __init__(self, connectivity: int) -> None: ...

    def num_objects(self) -> int: ...

    def add_tile(
        self,
        tile: numpy.ndarray,  # bool
        start: tuple[int, int, int],
        stop: tuple[int, int, int],
    ) -> None: ...

    def digest(self) -> int: ...

    def extract_tile(
        self,
        tile: numpy.ndarray,  # numpy.uint32
        start: tuple[int, int, int],
        stop: tuple[int, int, int],
    ) -> None: ...
