import cv2 as cv
import numpy as np
path="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample6.jpg"
img=cv.imread(path,cv.IMREAD_COLOR)
r,g,b=cv.split(img)
cv.imwrite("Red.jpg",r)
cv.imwrite("Green.jpg",g)
cv.imwrite("Blue.jpg",b)