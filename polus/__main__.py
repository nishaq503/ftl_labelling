import numpy
import ftl_labelling


arr = numpy.asarray([[1, 2, 3], [4, 5, 6]], dtype=numpy.float64)
ftl_labelling.mult(2., arr)
print(arr)
