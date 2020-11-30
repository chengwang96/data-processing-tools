# encoding: utf-8
"""
@author: Cheng Wang
@date: 2020/03/19
@last modified: 2020/03/19
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Times New Roman'


def InitPlot():
    plt.clf()
    plt.figure(figsize=(5, 3))


def PlotFunction(x, y, label='func'):
    plt.plot(x, y, label=label, linewidth='2')


def SaveFigure(labelx='probability of ground truth class', labely='weight', output_name=None):
    plt.xlabel(labelx, fontsize=16)
    plt.ylabel(labely, fontsize=16)

    plt.legend(loc='upper right', fontsize=16)
    plt.tick_params(labelsize=16)
    plt.grid()
    plt.tight_layout()

    if output_name == None:
        filename = 'loss.eps'
    else:
        filename = output_name

    plt.savefig(filename, dpi=300)


if __name__ == '__main__':
    InitPlot()
    x = np.linspace(0.0001, 1, 1000)
    y = - 0.25 * (1 - x) ** 2 * np.log(x)
    PlotFunction(x, y, 'focal loss')

    T = 0.3
    y = np.exp((1-x)/T) / 12
    PlotFunction(x, y, 'hardness')

    SaveFigure()
