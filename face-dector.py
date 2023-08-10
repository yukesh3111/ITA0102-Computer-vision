import cv2 as cv
face_cascade=cv.CascadeClassifier("C:\\Users\\NITHISH\\Desktop\\Opencv\\xml-file\\haarcascade-frontalface-default.xml")
path="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\group2.jpg"
img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(img,1.9,2)
for (x,y,w,h) in face:
    cv.rectangle(img,(x,y),(w+x,h+y),(255,0,0),20)
cv.imwrite("group_face_dection.jpg",img)