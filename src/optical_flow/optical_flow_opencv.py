import cv2
import numpy as np
import os.path as osp


frame1 = cv2.imread(osp.join('images', '399.jpg'))
frame2 = cv2.imread(osp.join('images', '401.jpg'))
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
print(flow)

# Change here
horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)
vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
horz = horz.astype('uint8')
vert = vert.astype('uint8')

# Change here too
cv2.imshow('Horizontal Component', horz)
cv2.imshow('Vertical Component', vert)

k = cv2.waitKey(0) & 0xff
if k == ord('s'): # Change here
    cv2.imwrite('opticalflow_horz.pgm', horz)
    cv2.imwrite('opticalflow_vert.pgm', vert)

cv2.destroyAllWindows()
