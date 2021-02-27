import numpy as np
import matplotlib.pyplot as plt
from common_tools.error import *
import matplotlib
matplotlib.rcParams['font.family'] = 'Times New Roman'


def plot_histogram(x, ys, labels, tick_label, save_path):
    plt.clf()
    plt.figure(figsize=(5, 3))
    size = len(x)

    total_width, n = 0.8, len(ys)
    width = total_width / n
    x = x - (total_width - width) / 2

    i = 0
    for y, label in zip(ys, labels):
        yn = [a / 10000 for a in y]
        plt.bar(x + i * width, yn, width=width, label=label, tick_label=tick_label)
        i += 1
    plt.title('{}'.format(save_path.split('.')[0]), fontsize='xx-large')
    plt.xlabel('IoU with GT Box', fontsize=16)
    plt.ylabel(r'Box number ($\times$10e4)', fontsize=16)
    plt.legend(fontsize=16)
    plt.tick_params(labelsize=16)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)

    return 0
