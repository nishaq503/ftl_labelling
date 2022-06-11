import logging

from . import constants


def make_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(constants.POLUS_LOG)
    return logger


def get_output_name(filename: str) -> str:
    name = filename.split('.ome')[0]
    return f'{name}{constants.POLUS_EXT}'


def tile_reading_indices(shape: tuple[int, int, int]) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    y_shape, x_shape, z_shape = shape
    xy_stride = constants.TILE_STRIDE_3D if z_shape == 1 else constants.TILE_STRIDE_2D
    z_stride = 1 if z_shape == 1 else constants.TILE_STRIDE_3D

    indices = list()
    for z in range(0, z_shape, z_stride):
        z_max = min(z_shape, z + z_stride)

        for y in range(0, y_shape, xy_stride):
            y_max = min(y_shape, y + xy_stride)

            for x in range(0, x_shape, xy_stride):
                x_max = min(x_shape, x + xy_stride)

                start = (y, x, z)
                end = (y_max, x_max, z_max)
                indices.append((start, end))

    return indices


def tile_writing_indices(shape: tuple[int, int, int]) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    y_shape, x_shape, z_shape = shape
    xy_stride = constants.TILE_STRIDE_2D

    indices = list()
    for z in range(z_shape):

        for y in range(0, y_shape, xy_stride):
            y_max = min(y_shape, y + xy_stride)

            for x in range(0, x_shape, xy_stride):
                x_max = min(x_shape, x + xy_stride)

                start = (y, x, z)
                end = (y_max, x_max, z + 1)
                indices.append((start, end))

    return indices
