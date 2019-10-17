# encoding: utf-8
"""
@author: zxcvb6958
@date: 2019/10/17
@last modified: 2019/10/17
"""

import pickle
import torch
import sys


def readPickle(input, from_python_type='3'):
    now_ver = sys.version[0]

    if from_python_type == now_ver:
        with open(input) as f:
            return pickle.loads(f.read())

    if from_python_type == '2' and now_ver == '3':
        with open(input) as f:
            return pickle.load(f, encoding='latin1')

    if from_python_type == '3' and now_ver == '2':
        raise Exception('You should save the pkl file by protocol=2 in Python3 firstly!')


def writePickle(data, save_path, to_python_type='3'):
    now_ver = sys.version[0]

    if now_ver == 2 or to_python_type == now_ver:
        with open(save_path) as f:
            f.write(pickle.dumps(data))

    if to_python_type == '2' and now_ver == '3':
        with open(save_path) as f:
            f.write(pickle.dumps(data, protocol=2))


def main():
    a_dict = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
    a_list = [a_dict, a_dict, 0]
    a_tensor = torch.Tensor([1, 2, 3])

    # save
    save_path = ['dict.pkl', 'list.pkl', 'tensor.pkl']
    writePickle(a_dict, save_path[0])
    writePickle(a_list, save_path[1])
    writePickle(a_tensor, save_path[2])

    # read
    print(readPickle(save_path[0]))
    print(readPickle(save_path[1]))
    print(readPickle(save_path[2]))
