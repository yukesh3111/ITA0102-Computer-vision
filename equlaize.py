import cv2
import numpy as np
img = cv2.imread(r'C:\Users\NITHISH\Desktop\Opencv\image\sample5.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imwrite('equlizehist.jpg', res)
