import logging

from . import constants


def make_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(constants.POLUS_LOG)
    return logger


def get_output_name(filename: str) -> str:
    name = filename.split('.ome')[0]
    return f'{name}{constants.POLUS_EXT}'
