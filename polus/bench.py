import logging
import pathlib
from time import time

from .utils import helpers
from . import polygons


logging.basicConfig(
    format='%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
)
logger = helpers.make_logger(__name__)


def bench(in_path: pathlib.Path, out_path: pathlib.Path):

    polygon_set = polygons.PyPolygonSet(connectivity=1)

    start = time.perf_counter()
    polygon_set.read_from(in_path)
    end = time.perf_counter()
    print(f'took {end - start:.3f} seconds to read and digest...')

    polygon_set.write_to(out_path)
    print(f'took {time.perf_counter() - end:.3f} seconds to write...')

    return
