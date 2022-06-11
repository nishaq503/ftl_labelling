import argparse
import logging
from pathlib import Path

from . import polygons as relabel
from .utils import helpers


logging.basicConfig(
    format='%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
)
logger = helpers.make_logger(__name__)


# Setup the argument parsing
logger.info("Parsing arguments...")
parser = argparse.ArgumentParser(
    prog='main',
    description='Label objects in a 2d or 3d binary image.',
)

parser.add_argument(
    '--inpDir', dest='inpDir', type=str, required=True,
    help='Input image collection to be processed by this plugin',
)

parser.add_argument(
    '--connectivity', dest='connectivity', type=str, required=True,
    help='City block connectivity, must be less than or equal to the number of dimensions',
)

parser.add_argument(
    '--outDir', dest='outDir', type=str, required=True,
    help='Output collection',
)

# Parse the arguments
args = parser.parse_args()

_connectivity = int(args.connectivity)
logger.info(f'connectivity = {_connectivity}')

_input_dir = Path(args.inpDir).resolve()
assert _input_dir.exists(), f'{_input_dir } does not exist.'
if _input_dir.joinpath('images').is_dir():
    _input_dir = _input_dir.joinpath('images')
logger.info(f'inpDir = {_input_dir}')

_output_dir = Path(args.outDir).resolve()
assert _output_dir.exists(), f'{_output_dir } does not exist.'
logger.info(f'outDir = {_output_dir}')

# Get all file names in inpDir image collection
_files = list(filter(
    lambda _file: _file.is_file() and _file.name.endswith('.ome.tif'),
    _input_dir.iterdir()
))

logger.info(f'Processing {len(_files)} images ...')


for i, in_file in enumerate(_files, start=1):
    logger.info(f'Relabelling {i}/{len(_files)} {in_file.name} ...')
    out_file = _output_dir.joinpath(helpers.get_output_name(in_file.name))
    relabel.PyPolygonSet(_connectivity).read_from(in_file).write_to(out_file)
