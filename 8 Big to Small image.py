import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample3.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
cv2.imwrite("Output/big_to_small_image.jpg",imgCanny)
cv2.waitKey(0)
