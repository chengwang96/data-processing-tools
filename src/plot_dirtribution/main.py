# encoding: utf-8
"""
@author: zxcvb6958
@date: 2019/10/17
@last modified: 2019/10/17
"""

from __future__ import print_function, absolute_import
import os
import argparse
import sys
sys.path.append('..')


from quick_restore.main import readPickle
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='Plot data distribution with line chart.')
parser.add_argument('--data', type=str, default='data.pkl', help="path to data (.pkl)")
parser.add_argument('-i', '--interval', type=int, default=1, help="The extend of each data point (default: 1%)")
parser.add_argument('-f', '--format', type=str, default='eps', help='file format (eps, jpg, png)', choices=['eps', 'jpg', 'png'])
parser.add_argument('-o', '--output', type=str, default='output', help='output floder')

args = parser.parse_args()


def plotDistribution(data, save_path):
    maximum = data.max()
    minimum = data.min()
    range = maximum - minimum

    counter = np.zeros((100 % args.interval))

    for item in data:
        index = int((item - minimum) / (range * args.interval / 100))
        counter[index] += 1

    x = np.linspace(0, 100 % args.interval, 100 % args.interval, endpoint=False)
    plt.plot(x, counter, linewidth='2')
    plt.savefig(save_path, dpi=300)


def main():
    if not os.path.exists(args.data):
        raise Exception("No such file: {}".format(args.data))

    print('Load pkl file...')
    all_data = readPickle(args.data)

    if 100 >= args.interval > 0 and 100 % args.interval == 0:
        if len(all_data) == 1:
            plotDistribution(all_data, os.path.join(args.output, 'result.{}'.format(args.format)))
        else:
            for i, data in enumerate(all_data):
                plotDistribution(data, os.path.join(args.output, 'result{}.{}'.format(i, args.format)))
    else:
        raise Exception('Interval is invalid!')


if __name__ == '__main__':
    main()
