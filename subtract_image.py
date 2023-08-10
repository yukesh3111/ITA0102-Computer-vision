import cv2 as cv
import numpy as np
path1="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample9.jpg"
path2="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample10.jpg"
img1=cv.imread(path1)
img2=cv.imread(path2)
sub=cv.subtract(img1,img2)
cv.imwrite("sub.jpg",sub)