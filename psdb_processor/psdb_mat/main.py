# encoding: utf-8
"""
@author: Cheng Wang
@date: 2019/10/17
@last modified: 2019/10/17
"""

from scipy.io import loadmat, savemat
import timeit
import os
import numpy as np
import cv2
import pickle
import tqdm
from common_tools.error import *


def read_mat(mat_file, output_list):
    data = loadmat(mat_file)
    for key in data.keys():
        if key == 'Img':
            output_list.append(data)
            return 0
        if not key.startswith('__'):
            output_list += data[key]
            return 0

    return 0


def write_mat(data, save_path='result.mat'):
    start = timeit.default_timer()

    if os.path.exists(save_path):
        os.remove(save_path)

    print('Start saving')
    savemat(save_path, data)

    print('OK')
    end = timeit.default_timer()
    print('Use time {0:.2f}s'.format(end - start))


def task(test, images):
    test_images_name = []
    test_images_count = 0
    for i in test:
        test_images_name.append(i[0][0])
        test_images_count += 1

    print('found {0} test images!'.format(test_images_count))

    processed_count = 0
    test_index = []
    all_size = []

    for i in images['Img'][0]:
        processed_count += 1
        if i[0][0] in test_images_name:
            test_index.append(processed_count - 1)

            boxes_count = 0
            size = []
            deleted_count = 0

            for box in i[2][0]:
                # print(box)
                box_size = int(box[0][0][2]) * int(box[0][0][3])
                size.append(box_size)
                all_size.append(box_size)

                if box_size > 10000:
                    # print(test_index[-1], '.', boxes_count - deleted_count, '.', boxes_count, '.', deleted_count)
                    np.delete(images['Img'][0][test_index[-1]][2][0], boxes_count - deleted_count, axis=0)
                    deleted_count += 1

                boxes_count += 1

    print('Processed {0} test images! {1} boxes'.format(processed_count, len(all_size)))
    return images


def cal_ratio(test, images):
    test_images_name = []
    test_images_count = 0
    for i in test:
        test_images_name.append(i[0][0])
        test_images_count += 1

    print('found {0} test images!'.format(test_images_count))

    w = []
    h = []
    size = []
    count = 0
    for i in images['Img'][0]:
        if i[0][0] in test_images_name:
            count += 1
            for box in i[2][0]:
                w.append(int(box[0][0][2]))
                h.append(int(box[0][0][3]))
                size.append(int(box[0][0][2]) * int(box[0][0][3]))

            if count % 1000 == 0:
                print("proceeded {0} images.".format(count))

    return sum(w) / sum(h), size


def le(size, threshold):
    size = np.array(size)
    return sum(size < threshold)


def convert_dataset(images):
    output_train = []
    output_test = []
    train, test = load_image_set_index()

    pbar = tqdm.tqdm(total=len(images['Img'][0]))
    for item in images['Img'][0]:
        output_item = {}
        output_item['filename'] = item[0][0]
        img = cv2.imread(os.path.join('SSM', item[0][0]))
        output_item['width'] = img.shape[1]
        output_item['height'] = img.shape[0]
        output_item['ann'] = {}
        all_boxes = [a[0][0] for a in item[2][0]]
        output_item['ann']['bboxes'] = np.array(all_boxes).astype(np.float32)
        output_item['ann']['labels'] = np.ones(len(all_boxes)).astype(np.int64)

        if item[0][0] in train:
            output_train.append(output_item)
        if item[0][0] in test:
            output_test.append(output_item)

        pbar.update(1)

    with open('mmdet_psdb_train.txt', 'w') as f:
        pickle.dump(output_train, f)
    with open('mmdet_psdb_test.txt', 'w') as f:
        pickle.dump(output_test, f)


def load_image_set_index():
    """
    Load the indexes for the specific subset (train / test).
    For PSDB, the index is just the image file name.
    """
    # test pool
    test = loadmat(os.path.join('ann', 'pool.mat'))
    test = test['pool'].squeeze()
    test = [str(a[0]) for a in test]
    # all images
    all_imgs = loadmat(os.path.join('ann', 'Images.mat'))
    all_imgs = all_imgs['Img'].squeeze()
    all_imgs = [str(a[0][0]) for a in all_imgs]
    # training
    train = list(set(all_imgs) - set(test))
    train.sort()

    return train, test


if __name__ == '__main__':
    image_path = 'ann/Images.mat'
    images = []
    check_error_code(read_mat(image_path, images))
    convert_dataset(images[0])
