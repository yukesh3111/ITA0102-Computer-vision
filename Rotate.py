import cv2 as cv
import numpy as np
path="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample3.jpg"
img=cv.imread(path)
angle=270
height,width=img.shape[:2]
center=(height//2,width//2)
rotate_matrix=cv.getRotationMatrix2D(center,angle,1.0)
rotate_image=cv.warpAffine(img,rotate_matrix,(height,width))
cv.namedWindow("output_image",cv.WINDOW_NORMAL)
cv.imshow("output_image",rotate_image)
cv.resizeWindow("output_image",800,650)
cv.waitKey(0)