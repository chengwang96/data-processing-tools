# encoding: utf-8
"""
@author: Cheng Wang
@date: 2019/10/17
@last modified: 2019/10/17
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from openpyxl import load_workbook
matplotlib.rcParams['font.family'] = 'Times New Roman'


def plot_xy(x, y, labelx='lr', labely='mAP', output_name='lr.eps'):
    plt.figure(figsize=(6, 3))

    plt.plot(x, y, linewidth='2')

    if output_name == None:
        filename = 'loss.eps'
    else:
        filename = output_name

    plt.xlabel(labelx, fontsize=16)
    plt.ylabel(labely, fontsize=16)
    plt.legend(loc='upper right', fontsize=16)
    plt.tick_params(labelsize=16)
    # plt.xlim((0, 9))
    plt.grid()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)


def plot_xyy(x, y1, y2, labelx='Epoch', labely='Loss', output_name=None):
    plt.figure(figsize=(6, 3))

    plt.plot(x, y1, label='baseline', linewidth='2')
    plt.plot(x, y2, label='hard-fine', linewidth='2')
    if output_name == None:
        filename = 'loss.eps'
    else:
        filename = output_name

    plt.xlabel(labelx, fontsize=16)
    plt.ylabel(labely, fontsize=16)
    plt.legend(loc='upper right', fontsize=16)
    plt.tick_params(labelsize=16)
    # plt.xlim((0, 9))
    plt.grid()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)


def plot_xy(x, y_list, output_dir=None):
    plt.figure(figsize=(7, 5))
    labels = ['TCTS', 'Reid_driven', 'OIM', 'NPSM', 'MGTS']
    shapes = ['rv-', '*-', 'x-', 'd-', 'bo-']
    for y, shape, this_label in zip(y_list, shapes, labels):
        plt.plot(x, y, shape, label=this_label, linewidth='2')

    if output_dir == None:
        filename = 'gallery_size.eps'
    else:
        filename = os.path.join(output_dir, 'gallery_size.eps')

    plt.xlabel('Gallery Size', fontsize=17)
    plt.ylabel('mAP(%)', fontsize=17)
    plt.legend(loc='best', fontsize=17, framealpha=0.5)
    plt.tick_params(labelsize=17)
    plt.ylim((30, 100))
    plt.grid()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)


def plot_9(x, y_list, output_dir=None):
    plt.figure(figsize=(7, 3))
    labels = ['Resnet50', 'Resnet50-FLGC', 'Resnet50-SGC']
    shapes = ['o-', '*-', 'x-']
    for y, shape, this_label in zip(y_list, shapes, labels):
        plt.plot(x, y, shape, label=this_label, linewidth='2')

    if output_dir == None:
        filename = '9.eps'
    else:
        filename = os.path.join(output_dir, '9.eps')

    plt.xlabel('Group Number', fontsize=17)
    plt.ylabel('Accuracy(%)', fontsize=17)
    plt.legend(loc='lower left', fontsize=17)
    plt.tick_params(labelsize=17)
    plt.grid()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)


def plot_decision(x, y_list, output_dir=None):
    plt.figure(figsize=(7, 3))
    labels = ['$2x_2=x_1$', '$2x_2=1-x_1$']
    for y, this_label in zip(y_list, labels):
        plt.plot(x, y, label=this_label, linewidth='2')

    plt.plot([0.5, 0.5], [-0.5, 1], label='$x_1=1/2$', linewidth='2')

    if output_dir == None:
        filename = 'decision.eps'
    else:
        filename = os.path.join(output_dir, 'decision.eps')

    plt.legend(loc='upper right', fontsize=15)
    plt.tick_params(labelsize=17)
    plt.xlim((-1, 4))
    plt.grid()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)


def input_data():
    wb = load_workbook('500.xlsx')
    print(wb.get_sheet_names())
    sheet = wb.active

    x, y1, y2 = [], [], []
    var_list = ['x', 'y1', 'y2']
    i = 0

    for column in sheet.columns:
        for cell in column:
            eval(var_list[i]).append(cell.value)
        i = i + 1

    return x, y1, y2


def input_data2():
    x = ['50', '100', '500', '1000', '2000', '4000']
    y1 = [94.5, 93.9, 90.8, 89.3, 86.7, 84.3]
    y2 = [94.0, 93.2, 89.7, 87.7, 85.1, 82.9]
    y3 = [79.4, 75.5, 65.7, 60.8, 56.5, 51.3]
    y4 = [81.6, 77.9, 68, 63.6, 58.3, 53.5]
    y5 = [84.8, 83, 76.9, 73.9, 70.2, 66.3]

    return x, [y1, y2, y3, y4, y5]


def input_data3():
    x = [2, 4, 8]
    y1 = [98.82, 98.82, 98.82]
    y2 = [98.82, 98.82, 98.73]
    y3 = [98.81, 98.78, 98.3]

    return x, [y1, y2, y3]


def input_data4():
    x = np.arange(-1, 2.5, 0.5)
    y1 = x/2
    y2 = (1-x)/2

    return x, [y1, y2]


def input_lr():
    x = [0.0, 1.0, 2.0, 5.0, 10.0]
    y = [ , , 94.5, , ,]

    return x, y


if __name__ == '__main__':
    # x, y1, y2 = input_data()
    # plot_xyy(x, y1, y2)

    m, n = input_data2()
    plot_xy(m, n)

    # x, y = input_data3()
    # plot_9(x, y)

    # plot_decision_boundary
    # x, y = input_data4()
    # plot_decision(x, y)
