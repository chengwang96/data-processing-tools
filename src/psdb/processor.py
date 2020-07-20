from scipy.io import loadmat, savemat
import cv2

dismiss_list = []

data = loadmat('Person.mat')['Person'][0]
for person in data:
    idname = int(person[0][0][1:])
    if idname in dismiss_list:
        continue
    nAppear = person[1][0][0]
    scences = person[2][0]
    if nAppear > 7 or nAppear < 5:
        continue
    index = 0
    for scence in scences:
        im_name = scence[0][0]
        box = scence[1][0]
        img = cv2.imread('/Users/wangcheng/Desktop/psdb/dataset/Image/SSM/' + im_name)
        x = int(box[1])+int(box[3])
        y = int(box[0])+int(box[2])
        target = img[int(box[1]):int(box[1])+int(box[3]), int(box[0]):int(box[0])+int(box[2]), :]
        cv2.imwrite(str(idname) + '_' + str(index) + '.jpg', target)
        index += 1
