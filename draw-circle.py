import numpy as np  
import cv2  
img = cv2.imread(r'C:\Users\NITHISH\Desktop\Opencv\image\person.jpg',1)  
cv2.circle(img,(80,80), 55, (0,255,0), -1)  
cv2.imwrite('circle-image.jpg',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  