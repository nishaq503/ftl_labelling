import gc
import pathlib
import typing

import bfio
import bfio.OmeXml
import ftl_labelling
import numpy

from . import utils
from .utils import constants
from .utils import helpers

logger = helpers.make_logger(__name__)


class PyObjectSet:

    def __init__(self, connectivity: int):
        if not (1 <= connectivity <= 3):
            message = f'connectivity must be 1, 2 or 3. Got {connectivity} instead'
            logger.error(message)
            raise ValueError(message)

        self.__connectivity: int = connectivity
        self.__metadata: typing.Union[bfio.OmeXml.OMEXML, utils.Unset] = constants.UNSET
        self.__num_objects: typing.Union[int, utils.Unset] = constants.UNSET
        self.__polygon_set = ftl_labelling.ObjectSet(connectivity)

    @property
    def connectivity(self) -> int:
        return self.__connectivity

    @property
    def metadata(self) -> bfio.OmeXml.OMEXML:
        if isinstance(self.__metadata, utils.Unset):
            message = f'Please call `read_from` before using this property.'
            logger.error(message)
            raise ValueError(message)

        return self.__metadata

    @property
    def num_objects(self) -> int:
        if isinstance(self.__metadata, utils.Unset):
            message = f'Please call `read_from` before using this property.'
            logger.error(message)
            raise ValueError(message)

        return self.__num_objects

    def read_from(self, path: pathlib.Path) -> 'PyObjectSet':

        with bfio.BioReader(path) as reader:
            self.__metadata = reader.metadata

            shape = (reader.Y, reader.X, reader.Z)
            indices = helpers.tile_reading_indices(shape)

            for i, (start, stop) in enumerate(indices, start=1):
                y_min, x_min, z_min = start
                y_max, x_max, z_max = stop

                logger.debug(f'Adding tile {i}/{len(indices)} ...')

                tile = numpy.squeeze(reader[y_min:y_max, x_min:x_max, z_min:z_max, 0, 0])
                tile = numpy.asarray(tile > 0, dtype=numpy.bool_)
                if tile.ndim == 2:
                    tile = tile[:, :, None]
                tile = tile.transpose([2, 0, 1])

                self.__polygon_set.add_tile(tile, start, stop)

        logger.debug(f'Digesting objects ...')
        self.__num_objects = self.__polygon_set.digest()
        logger.debug(f'Collected {self.num_objects} objects ...')

        return self

    def write_to(self, path: pathlib.Path):

        with bfio.BioWriter(path, metadata=self.metadata, max_workers=constants.NUM_WORKERS) as writer:
            writer.dtype = numpy.uint32

            shape = (writer.Y, writer.X, writer.Z)
            indices = helpers.tile_writing_indices(shape)

            for i, (start, stop) in enumerate(indices, start=1):
                y_min, x_min, z_min = start
                y_max, x_max, z_max = stop

                logger.debug(f'Writing tile {i}/{len(indices)} ...')

                tile = numpy.zeros(shape=(z_max - z_min, y_max - y_min, x_max - x_min), dtype=numpy.uint32)
                self.__polygon_set.extract_tile(tile, start, stop)
                tile = tile.transpose([1, 2, 0])
                writer[y_min:y_max, x_min:x_max, z_min:z_max] = tile

        del self.__polygon_set
        gc.collect()

        self.__polygon_set = None
        return


__all__ = [
    'PyObjectSet',
]
