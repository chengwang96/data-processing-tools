import cv2
import tqdm
from common_tools.error import *
from common_tools.file_op import *


def crop_bbox(data_dir, boxes, save_dir):
    gt_save_dir = save_dir + '/gt_boxes'
    det_save_dir = save_dir + '/det_boxes'

    check_error_code(mkdir_if_missing(save_dir))
    check_error_code(mkdir_if_missing(gt_save_dir))
    check_error_code(clean_and_mkdir(det_save_dir))

    pbar = tqdm.tqdm(total=len(boxes))
    for item in boxes:
        im_name = item['im_name']
        gt_boxes = item['gt_boxes']
        det_boxes = item['det_boxes'].astype(int)
        det_scores = item['det_scores']
        if 'det_ious' not in item:
            continue
        det_ious = item['det_ious']

        image = cv2.imread(os.path.join(data_dir, im_name))
        for i, gt_box in enumerate(gt_boxes):
            cv2.imwrite(os.path.join(gt_save_dir, '{}_{}.jpg'.format(im_name.split('.')[0], i)),
                        image[gt_box[1]:gt_box[3], gt_box[0]:gt_box[2], :])

        for i, det_box in enumerate(det_boxes):
            size = (det_box[3] - det_box[1]) * (det_box[2] - det_box[0])
            if 0.6 > det_ious[i] > 0.4 and size > 9000:
                cv2.imwrite(os.path.join(det_save_dir, '{}_{:.2f}_{:.2f}_{}.jpg'.format(im_name.split('.')[0], det_ious[i],
                            det_scores[i], i)), image[det_box[1]:det_box[3], det_box[0]:det_box[2], :])

        pbar.update(1)

    return 0
