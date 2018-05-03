import cv2
from skimage.measure import compare_ssim
import os
import os.path as osp


def save_image(X):
    image_root = 'pic'
    file = open(osp.join(image_root, 'pixel.txt'), 'a')

    for pixel in X:
        file.write(str(list(pixel)))
        file.write('\n')

    file.close()


def get_ssim(X, Y):
    w = Y.shape[0]
    h = Y.shape[1]
    X = X[:w, :h, :]
    # save_image(Y)
    # input()

    return compare_ssim(X, Y, multichannel=True)


def black2white(X):
    count = 0

    for i in X:
        for j in i:
            if j[0] == 0 and j[1] == 0 and j[2] == 0:
                count += 1
                for k in range(3):
                    j[k] = 0

    print(count)
    return X


if __name__ == '__main__':
    image_root = 'pic'
    save_root = 'new'
    X_root = osp.join(image_root, 'sketch_p2p')
    Y_root = osp.join(image_root, 'sketch_real')

    X_images = os.listdir(X_root)
    Y_images = os.listdir(Y_root)
    ssim = []

    for X_image, Y_image in zip(X_images, Y_images):
        print('{0} vs {1}'.format(X_image, Y_image))
        X = cv2.imread(osp.join(X_root, X_image))
        Y = cv2.imread(osp.join(Y_root, Y_image))
        X = cv2.resize(X, (250, 250), interpolation=cv2.INTER_LANCZOS4)
        result = get_ssim(X, Y)
        print(result)
        ssim.append(float(result))
        # process images
        # X = cv2.imread(osp.join(X_root, X_image))
        # Y = cv2.imread(osp.join(Y_root, Y_image))
        # X = black2white(X)
        # print(X.shape)
        # cv2.imwrite(osp.join(save_root, X_image), X)

    print('average: %f' % (sum(ssim) / len(ssim)))
    print('done')
