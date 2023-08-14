import cv2 as cv
import numpy as np
path1=r"C:\Users\NITHISH\Desktop\Opencv\image\sample17.png"
path2=r"C:\Users\NITHISH\Desktop\Opencv\image\sample3.jpg"

img1=cv.imread(path1)
img2=cv.imread(path2)
gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

resize_img1=cv.resize(img1,(1000,1000),interpolation=cv.INTER_LINEAR)
resize_img2=cv.resize(img2,(1000,1000),interpolation=cv.INTER_LINEAR)
not_operator=cv.bitwise_not(resize_img1)
add=cv.addWeighted(resize_img2,1.0,not_operator,2.2,0)
cv.imwrite("watermark_image.jpg",add)