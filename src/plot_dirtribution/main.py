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


parser = argparse.ArgumentParser(description='Plot data distribution with line chart.')
parser.add_argument('--data', type=str, default='data.pkl', help="path to data (.pkl)")
parser.add_argument('-i', '--interval', type=float, default=0.01, help="The extend of each data point (default: 1%)")
parser.add_argument('-f', '--format', type=str, default='eps', help='file format (eps, jpg, png)', choices=['eps', 'jpg', 'png'])
parser.add_argument('-o', '--output', type=str, default='output', help='output floder')

args = parser.parse_args()


def main():
    if not os.path.exists(args.data):
        raise Exception("No such file: {}".format(args.data))

    with open(args.data) as f:
        print('Load pkl file...')
        all_data = readPickle(args.data)


if __name__ == '__main__':
    main()
