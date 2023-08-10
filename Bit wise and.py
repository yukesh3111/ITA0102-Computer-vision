import cv2 as cv
import numpy as np
path1="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample11.png"
path2="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample12.png"
img1=cv.imread(path1)
img2=cv.imread(path2)
and_operator=cv.bitwise_and(img1,img2,mask=None)
cv.imwrite("AND_operator.png",and_operator)