import cv2 as cv
import numpy as np
path="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample14.png"
img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gauss=cv.GaussianBlur(gray,(5,5),0)
soble_x=cv.Sobel(gauss,cv.CV_8U,1,0,ksize=5)
soble_y=cv.Sobel(gauss,cv.CV_8U,0,1,ksize=5)
soble=cv.add(soble_x,soble_y)
cv.imwrite("Soble.png",soble)


