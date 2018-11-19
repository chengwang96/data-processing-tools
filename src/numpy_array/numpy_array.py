import numpy


# (1, 100) -> (25, 4)
a = numpy.arange(100).reshape(25, 4).tolist()


# (1, 5) + (1, 5) = (2, 5)
b = numpy.arange(5).reshape(1, 5)
c = numpy.arange(5).reshape(1, 5)
d = numpy.vstack((b, c))
# print(d.shape)
# print(d)

def func(x):
    print('1')
    import pdb; pdb.set_trace()


e = numpy.array([[[1, 2, 3], [4, 5, 6]], [[6, 5, 4], [3, 2, 1]]])
f = numpy.array([[[1, 2, 3], [4, 5, 6]], [[0, 0, 0], [0, 0, 0]]])
print(f == [0, 0, 0])
map(func, f)
import pdb; pdb.set_trace()
map(lambda x: x ** 2, numpy.array([1, 2, 3, 4, 5]))

print(f)
