import skimage.measure as skm
import cv2
import os.path as osp
import os
import pdb
from math import sqrt


def my_ssim(x, y):
    # pdb.set_trace()
    # h = y.shape[0]
    # w = y.shape[1]
    # x = x[:h, :w, :]
    K1 = 0.01; K2 = 0.03; L = 255
    C1 = pow(K1 * L, 2); C2 = pow(K2 * L, 2); C3 = C2 / 2

    mx = x.mean()
    my = y.mean()
    oxx = sqrt(variance(x, x))
    oyy = sqrt(variance(y, y))
    oxy = variance(x, y)

    L = (2*mx*my + C1) / (pow(mx, 2) + pow(my, 2) + C1)
    C = (2*oxx*oyy + C2) / (pow(oxx, 2) + pow(oyy, 2) + C2)
    S = (oxy + C3) / (oxx*oyy + C3)

    file = open('result.txt', 'a')
    file.write('L: {0}\nC: {1}\nS: {2}\n\n'.format(L, C, S))

    return L*C*S

def variance(x ,y):
    mx = x.mean()
    my = y.mean()
    h = y.shape[0]
    w = y.shape[1]
    c = 3
    sum = 0

    for i in range(h):
        for j in range(w):
            for k in range(3):
                sum += (x[i, j, k] - mx) * (y[i, j, k] - my)

    sum /= h*w*c - 1

    return sum

def ssim(x, y):
    # y = y[60:70, 60:70, :]
    # x = x[60:70, 60:70, :]
    h = y.shape[0]
    w = y.shape[1]
    x = x[:h, :w, :]

    # print(pytorch_ssim.ssim(x, y))
    return skm.compare_ssim(x, y, multichannel=True)


if __name__ == '__main__':
    pathX = 'pic\sketch_cycle'
    pathY = 'pic\sketch_p2p'

    fileX = os.listdir(pathX)
    fileY = os.listdir(pathY)
    result = []
    count = 0

    for imageX, imageY in zip(fileX, fileY):
        count += 1
        imageX = osp.join(pathX, imageX)
        imageY = osp.join(pathY, imageY)
        x = cv2.imread(imageX)
        y = cv2.imread(imageY)
        # x = cv2.resize(x, (250, 250), interpolation=cv2.INTER_LANCZOS4)

        result.append(my_ssim(x, y))

        if count % 10 == 0:
            print('{0} pairs done'.format(count))

    print(sum(result) / len(result))
