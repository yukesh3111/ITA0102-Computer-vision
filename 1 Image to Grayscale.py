import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample1.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("Output/GrayScale.jpg",imgGray)
cv2.waitKey(0)
