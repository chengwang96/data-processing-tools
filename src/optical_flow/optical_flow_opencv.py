import cv2
import numpy as np
import os.path as osp


frame1 = cv2.imread(osp.join('images', '399.jpg'))
frame2 = cv2.imread(osp.join('images', '401.jpg'))
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
print(flow.shape)
print(frame1.shape)
print(frame2.shape)
