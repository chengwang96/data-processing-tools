import numpy


# (1, 100) -> (25, 4)
a = numpy.arange(100).reshape(25, 4).tolist()


# (1, 5) + (1, 5) = (2, 5)
b = numpy.arange(5).reshape(1, 5)
c = numpy.arange(5).reshape(1, 5)
d = numpy.vstack((b, c))
# print(d.shape)
# print(d)
