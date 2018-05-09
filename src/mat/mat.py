from scipy.io import loadmat, savemat
import timeit
import os
import numpy as np

DEBUG = True


def readMat(mat_file):
    data = loadmat(mat_file)
    # data = loadmat(mat_file)['img_index_test'].squeeze()
    # data = loadmat(mat_file)['pool'].squeeze()
    # data = loadmat(mat_file)['Img'].squeeze()
    # print(data.keys())
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


def task(test, images):
    test_images_name = []
    test_images_count = 0
    for i in test:
        test_images_name.append(i[0][0])
        test_images_count += 1

    print('found {0} test images!'.format(test_images_count))

    #-------------- delete > 10000 --------------
    processed_count = 0
    test_index = []
    all_size = []

    for i in images['Img'][0]:
        processed_count += 1
        if i[0][0] in test_images_name:
            # print(i[0][0])
            # print(i[1][0])
            # print(i[2][0])
            # print('---------')
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

    # while 1:
    #     print('lower bounding:')
    #     x = input()
    #     print('upper bounding:')
    #     y = input()
    #     bigger = [int(y) > int(size) >= int(x) for size in all_size]
    #     print('{0} / {1}'.format(sum(bigger), len(all_size)))


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
    return sum(sum(np.where(size < threshold)))


if __name__ == '__main__':
    test_path = "pool.mat"
    image_path = "Images.mat"
    test = readMat(test_path)
    images = readMat(image_path)
    # images = task(test, images)
    # writeMat(images, 'NewImages.mat')
    _, size = cal_ratio(test, images)
    while 1:
        x = int(input('x = '))
        p2 = le(size, x * x)
        p3 = le(size, x * x * 4) - p2
        p4 = le(size, x * x * 16) - p2 - p3
        p5 = le(size, x * x * 64) - p2 - p3 - p4
        print((p2 - 0.0) / (p2 + p3 + p4 + p5))
        print((p3 - 0.0) / (p2 + p3 + p4 + p5))
        print((p4 - 0.0) / (p2 + p3 + p4 + p5))
        print((p5 - 0.0) / (p2 + p3 + p4 + p5))

    # print(le(size, 1000))
