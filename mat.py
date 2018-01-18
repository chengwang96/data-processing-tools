from scipy.io import loadmat, savemat
import numpy
import timeit
import os


def readMat(mat_file):
    # data = loadmat(mat_file)
    # data = loadmat(mat_file)['img_index_test'].squeeze()
    # data = loadmat(mat_file)['pool'].squeeze()
    data = loadmat(mat_file)['Img'].squeeze()
    # print(data.keys())
    print(data[0])
    print(len(data))


def pool(pool_path, save_path='.'):
    start = timeit.default_timer()

    data = loadmat(pool_path)
    data['pool'] = data.pop('img_index_test')
    # print(data.keys())
    if os.path.exists(save_path):
        os.remove(save_path)
        print(save_path.split('\\')[-1] + ' exists, it will be delete first')

    savemat(save_path, data)

    print('Change img_index_test to pool. OK')
    end = timeit.default_timer()
    print('Use time {0:.2f}s'.format(end - start))


def image(image_root, save_path):
    mats = os.listdir(image_root)

    for image in mats:
        if image.endswith('.mat'):



if __name__ == '__main__':
    # Pool
    # example = 'C:\\Users\\Cheng\\Desktop\\dataset\\annotation\\pool.mat'
    # readMat(example)
    # pool_path = 'C:\\Users\\Cheng\\Desktop\\PRW-v16.04.20\\frame_test.mat'
    # save_path = 'C:\\Users\\Cheng\\Desktop\\PRW-v16.04.20\\annotation\\pool.mat'
    # pool(pool_path, save_path)

    # Images
    example = 'C:\\Users\\Cheng\\Desktop\\dataset\\annotation\\Images.mat'
    readMat(example)
    image_root = 'C:\\Users\\Cheng\\Desktop\\PRW-v16.04.20\\annotations\\'
    save_path = 'C:\\Users\\Cheng\\Desktop\\PRW-v16.04.20\\annotation\\Images.mat'


    # Person


    # TestGXX


    # Train


    # mat_file = 'C:\\Users\\Cheng\\Desktop\\PRW-v16.04.20\\frame_test.mat'
    # mat_file = 'C:\\Users\\Cheng\\Desktop\\dataset\\annotation\\pool.mat'
    # readMat(mat_file)
