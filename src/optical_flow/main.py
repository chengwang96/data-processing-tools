# encoding: utf-8
"""
@author: zxcvb6958
@date: 2019/10/17
@last modified: 2019/10/17
"""

import cv2
import numpy as np
import copy
INF = 255


def is_empty(x, y, u):
    if u[x][y][0] == INF and u[x][y][1] == INF:
        return True

    return False


def image_add(It, x, y, I0, x0, y0, I1, x1, y1):
    for i in range(3):
        It[x][y][i] = I0[x0][y0][i] / 2 + I1[x1][y1][i] / 2

    return It


def position_is_legal(x, y, height, width):
    if height > x >= 0 and width > y >= 0:
        return True

    return False


# Compute optical flow in time t(=0.5)
def compute_flow(u0):
    ut = copy.deepcopy(u0)
    height = u0.shape[0]
    width = u0.shape[1]

    for x in range(height):
        for y in range(width):
            ut[x][y][0] = INF
            ut[x][y][1] = INF

    for x in range(height):
        for y in range(width):
            x_new = int(round(x + u0[x][y][0]))
            y_new = int(round(y + u0[x][y][1]))
            if position_is_legal(x_new, y_new, height, width):
                ut[x_new][y_new] = u0[x][y]

    x_splats = [-1, 0, 1]
    y_splats = [-1, 0, 1]
    count, x_sum, y_sum = 0, 0, 0
    for x in range(height):
        for y in range(width):
            if is_empty(x, y, ut):
                for x_splat in x_splats:
                    for y_splat in y_splats:
                        x_new = int(round(x + x_splat))
                        y_new = int(round(y + y_splat))
                        if position_is_legal(x_new, y_new, height, width):
                            if not is_empty(x_new, y_new, ut):
                                x_sum += ut[x_new][y_new][0]
                                y_sum += ut[x_new][y_new][1]
                                count = count + 1

                if count == 0:
                    ut[x][y][0], ut[x][y][1] = 0, 0
                else:
                    ut[x][y][0], ut[x][y][1] = x_sum / count, y_sum / count

    return ut


# Splat optical flow to keep photo consistency
def splat_flow(u, I0, I1):
    height = u0.shape[0]
    width = u0.shape[1]
    x_splats = [-1, 0, 1]
    y_splats = [-1, 0, 1]

    for x in range(height):
        for y in range(width):
            min_dis = INF
            best_u = copy.deepcopy(u[x][y])

            for x_splat in x_splats:
                for y_splat in y_splats:
                    if position_is_legal(x + x_splat, y + y_splat, height, width):
                        temp = u[x+x_splat][y+y_splat]
                        x_new = int(round(x + temp[0] / 2))
                        y_new = int(round(y + temp[1] / 2))
                        if position_is_legal(x_new, y_new, height, width):
                            if abs(I0[x][y] - I1[x_new][y_new]) < min_dis:
                                best_u = temp

            u[x][y] = best_u

    return u


# Compute the colors of the interpolated pixels
def interpolate(I0, I1, ut):
    height = u0.shape[0]
    width = u0.shape[1]
    It = copy.deepcopy(I0)

    for x in range(height):
        for y in range(width):
            It[x][y] = 0

    for x in range(height):
        for y in range(width):
            x0 = int(round(x - ut[x][y][0] / 2))
            y0 = int(round(y - ut[x][y][1] / 2))
            x1 = int(round(x + ut[x][y][0] / 2))
            y1 = int(round(y + ut[x][y][1] / 2))
            if position_is_legal(x0, y0, height, width):
                if position_is_legal(x1, y1, height, width):
                    It = image_add(It, x, y, I0, x0, y0, I1, x1, y1)
                else:
                    It = image_add(It, x, y, I0, x0, y0, I0, x0, y0)
            else:
                if position_is_legal(x1, y1, height, width):
                    It = image_add(It, x, y, I1, x1, y1, I1, x1, y1)

    return It


if __name__ == '__main__':
    file_index = np.linspace(399, 541, 72)
    for index in file_index:
        file1 = int(index)
        file2 = int(index + 2)
        file_out = int(index + 1)
        print('interpolate frame {0}'.format(file_out))
        if file2 > file_index[-1]:
            break

        str_first = './images/' + str(file1) + '.jpg'
        str_second = './images/' + str(file2) + '.jpg'
        str_out = str(file_out) + '.jpg'

        frame1 = cv2.imread(str_first)
        frame2 = cv2.imread(str_second)
        prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        u0 = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        u0 = splat_flow(u0, prvs, next)
        ut = compute_flow(u0)
        It = interpolate(frame1, frame2, ut)
        cv2.imwrite(str_out, It)
