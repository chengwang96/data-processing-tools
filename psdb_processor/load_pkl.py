import pickle
import numpy as np
from common_tools.error import *


def load_tcts_pkl(pkl_file):
    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)

    det_ious = np.array([])
    for item in data:
        if 'det_ious' in item:
            det_ious = np.append(det_ious, item['det_ious'])

    print('len(det_ious)={}'.format(len(det_ious)))
    print('sum(det_ious > 0.5)={}'.format(sum(det_ious > 0.5)))
    print('sum(det_ious > 0.9)={}'.format(sum(det_ious > 0.9)))
    print('sum(0.9 > det_ious > 0.8)={}'.format(sum(det_ious > 0.8) - sum(det_ious > 0.9)))
    print('sum(0.8 > det_ious > 0.7)={}'.format(sum(det_ious > 0.7) - sum(det_ious > 0.8)))
    print('sum(0.7 > det_ious > 0.6)={}'.format(sum(det_ious > 0.6) - sum(det_ious > 0.7)))
    print('sum(0.6 > det_ious > 0.5)={}'.format(sum(det_ious > 0.5) - sum(det_ious > 0.6)))

    return 0


def load_mmdet_pkl():
    return -1
