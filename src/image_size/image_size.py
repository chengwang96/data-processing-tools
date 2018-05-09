import cv2
import os
import pdb


img = cv2.imread('1.jpg')
pdb.set_trace()
dataset_name = 'coco'
root_dir = "data"
image_list = os.listdir(root_dir)
size_list = []
count = 0

for image in image_list:
    im = cv2.imread(os.path.join(root_dir, image))
    # print(image)
    count += 1
    if count % 100 == 0:
        print('Proceeded {0} images'.format(count))
    if im.shape[:2] not in size_list and im.shape[1::-1] not in size_list:
        size_list.append(im.shape[:2])

print('OK!')
print(size_list)
f = open(dataset_name + '.txt', 'w')
f.write(size_list)
