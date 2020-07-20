# encoding: utf-8
"""
@author: Cheng Wang
@date: 2020/05/07
@last modified: 2020/05/07
"""

from scipy.io import loadmat, savemat
import timeit
import os
import numpy as np

DEBUG = True


def ReadMat(mat_file):
    data = loadmat(mat_file)
    for key in data.keys():
        if key == 'Img':
            return data
        if not key.startswith('__'):
            return data[key]

    print('no data!')
    return 0


def writeMat(data, save_path='result.mat'):
    start = timeit.default_timer()

    if os.path.exists(save_path):
        os.remove(save_path)

    print('Start saving')
    savemat(save_path, data)

    print('OK')
    end = timeit.default_timer()
    print('Use time {0:.2f}s'.format(end - start))


if __name__ == '__main__':
    test_path = "TestG50.mat"
    # image_path = "Images.mat"
    train_path = "Train.mat"
    person_path = "Person.mat"
    test = ReadMat(test_path)
    # images = ReadMat(image_path)
    train = ReadMat(train_path)
    persons = ReadMat(person_path)[0]
    forward_sum = 0

    print(test)
    print(test[0])
    print(test[0][0])

    for person in persons:
        appear_num = person[1][0][0]
        # forward_sum = forward_sum + appear_num
        # forward_sum = forward_sum + (appear_num-1) * appear_num
        if appear_num == 1:
            continue
        for i in range(appear_num):
            appear_info = person[2][0][i]

    for train_person in train:
        person_id = train_person[0][0][0][0][0]
        appear_num = train_person[0][0][0][1][0][0]
        forward_sum = forward_sum + (appear_num - 1) * appear_num
        # print(train_person[0][0][0][2][0][0])

    print("total num of train set:{}".format(forward_sum))
