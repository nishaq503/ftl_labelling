from this import s
import ftl_labelling
import numpy


def main():
    obj = ftl_labelling.PolygonSet(connectivity=1)

    tile = numpy.zeros(shape=(100, 100, 100), dtype=bool)
    start = (100, 100, 100)
    stop = (200, 200, 200)

    obj.add_tile(tile, start, stop)

    obj.digest()

    print(f'num_objects: {obj.num_objects()}')

    tile = numpy.asarray(tile, dtype=numpy.uint32)
    obj.extract_tile(tile, start, stop)

    return


if __name__ == '__main__':
    main()
