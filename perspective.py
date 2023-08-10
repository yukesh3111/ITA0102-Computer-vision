import cv2
import numpy as np
img = cv2.imread(r"C:/Users/NITHISH/Desktop/Opencv/image/sample14.png")
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols, rows))
cv2.imwrite('Output18_Transformed_Image.jpg', dst)
cv2.imwrite('Output18_Original_Image.jpg',img)