import cv2 as cv
import numpy as np
path="C:/Users/NITHISH/Desktop/Opencv/image/sample14.png"
image=cv.imread(path)
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
img_gauss=cv.GaussianBlur(gray,(3,3),0)
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv.filter2D(img_gauss, -1, kernelx)
img_prewitty = cv.filter2D(img_gauss, -1, kernely)
cv.imwrite("Output15_PrewittX.jpg", img_prewittx)
cv.imwrite("Output15_PrewittY.jpg", img_prewitty)
cv.imwrite("Output15_Prewitt.jpg", img_prewittx + img_prewitty)
