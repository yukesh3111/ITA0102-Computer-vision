import cv2
import numpy as np
img = cv2.imread(r"C:\Users\NITHISH\Desktop\Opencv\image\gtr.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cascade = cv2.CascadeClassifier(r"C:\Users\NITHISH\Desktop\Opencv\xml-file\haarcascade_russian_plate_number.xml")
plates = cascade.detectMultiScale(gray, 1.2, 5)
print('Number of detected license plates:', len(plates))
for (x,y,w,h) in plates:
   cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray[y:y+h, x:x+w]
   color_plates = img[y:y+h, x:x+w]
   cv2.imshow('Output27_Numberplate', gray_plates)
   cv2.imshow('Output27_NumberPlate_Image', img)
   cv2.waitKey(0)
cv2.destroyAllWindows()