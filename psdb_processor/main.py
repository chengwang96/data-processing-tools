from psdb_processor.crop_bbox import crop_bbox
import pickle
from common_tools.error import *


if __name__ == '__main__':
    with open('train.pkl', 'rb') as f:
        train = pickle.load(f)
        check_error_code(crop_bbox('SSM', train, 'cropped_train'))
    with open('test.pkl', 'rb') as f:
        test = pickle.load(f)
        check_error_code(crop_bbox('SSM', test, 'cropped_test'))
