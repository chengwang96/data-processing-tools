import numpy


# (1, 100) -> (25, 4)
a = numpy.arange(100).reshape(25, 4).tolist()


# (1, 5) + (1, 5) = (2, 5)
b = numpy.arange(5).reshape(1, 5)
c = numpy.arange(5).reshape(1, 5)
d = numpy.vstack((b, c))
# print(d.shape)
# print(d)


# e.shape[0] = 4, get 0, 1, 3
e = numpy.vstack((d, d))
f = numpy.array([0, 1, 3])
# print(e[f])


# obtain a/several column(s)
g = numpy.array([[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])
h = g[:, 0]
i = g[:, 1:5]
# print(h)
# print(i)


# add a fake dimension
j = numpy.array([0, 1, 3])
j.reshape((1, 3))
# print(j.shape)


# transform list(s) into numpy array
k = [0, 1, 2, 3, 4]
l = [0, 1, 2, 3, 4]
l = [i+5 for i in l]
m = [0, 1, 2, 3, 4]
m = [i+5 for i in m]
n = numpy.array(k+l+m)
print(n)

