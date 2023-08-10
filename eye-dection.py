import cv2 as cv
eye_cascade=cv.CascadeClassifier("C:\\Users\\NITHISH\\Desktop\\Opencv\\xml-file\\haarcascade_eye.xml")
img=cv.imread("C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\group.jpg")
eye=eye_cascade.detectMultiScale(img,1.34,9)
for (x,y,w,h) in eye:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),8)
cv.imwrite("eye_dection.jpg",img)