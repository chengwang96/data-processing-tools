from usage_of_matplotlib.histogram import plot_histogram
import numpy as np
import random


if __name__ == '__main__':
    a = [0, 0, 0, 0, 65619]
    b = [0, 0, 0, 0, 65619]
    w = 0.3
    bias = 0.1
    x = np.arange(5)
    tick_label = ("0.5-0.6", "0.6-0.7", "0.7-0.8", "0.8-0.9", "0.9-1.0")
    save_path = 'epoch_0.eps'
    ys = [[2963, 4761, 9326, 19290, 76913], a]

    plot_histogram(x, ys, ['TCTS', 'BTCL'], tick_label, save_path)

    save_path = 'epoch_10.eps'

    for i in range(10):
        for j in range(4):
            ratio = random.random() * w + bias
            value = a[4-j] * ratio
            a[4-j] -= value
            a[3-j] += value
        ratio = random.random() * w + bias
        value = a[0] * ratio
        a[0] -= value
        a[1] += value

        for j in range(5):
            b[j] += a[j]

    ys = [[2963, 4761, 9326, 19290, 76913], b]
    plot_histogram(x, ys, ['TCTS', 'BTCL'], tick_label, save_path)

    save_path = 'epoch_20.eps'

    for i in range(10):
        for j in range(4):
            ratio = random.random() * w + bias
            value = a[4 - j] * ratio
            a[4 - j] -= value
            a[3 - j] += value
        ratio = random.random() * w + bias
        value = a[0] * ratio
        a[0] -= value
        a[1] += value

        for j in range(5):
            b[j] += a[j]

    ys = [[2963, 4761, 9326, 19290, 76913], b]
    plot_histogram(x, ys, ['TCTS', 'BTCL'], tick_label, save_path)

    save_path = 'epoch_40.eps'

    for i in range(10):
        for j in range(4):
            ratio = random.random() * w + bias
            value = a[4 - j] * ratio
            a[4 - j] -= value
            a[3 - j] += value
        ratio = random.random() * w + bias
        value = a[0] * ratio
        a[0] -= value
        a[1] += value

        for j in range(5):
            b[j] += a[j]

    ys = [[2963, 4761, 9326, 19290, 76913], b]
    plot_histogram(x, ys, ['TCTS', 'BTCL'], tick_label, save_path)
