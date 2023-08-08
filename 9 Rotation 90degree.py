import cv2
path ="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\sample4.jpg"
src = cv2.imread(path)
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("Output/rotate-90.jpg", image)
cv2.waitKey(0)