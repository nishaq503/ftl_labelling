import logging
import os


POLUS_LOG = getattr(logging, os.environ.get('POLUS_LOG', 'INFO'))
POLUS_EXT = os.environ.get('POLUS_EXT', '.ome.tif')
