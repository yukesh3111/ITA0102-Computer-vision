import cv2 as cv
import numpy as np
path1="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample7.jpg"
path2="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample8.jpg"
img1=cv.imread(path1)
img2=cv.imread(path2)
add=cv.addWeighted(img1,0.4,img2,0.5,0)
cv.imwrite("add_image.jpg",add)