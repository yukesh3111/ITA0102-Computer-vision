import cv2 as cv
smile_cascade=cv.CascadeClassifier("C:\\Users\\NITHISH\\Desktop\\Opencv\\xml-file\\haarcascade_smile.xml")
path="C:\\Users\\NITHISH\\Desktop\\Opencv\\image\\person2.jpg"
img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
smile=smile_cascade.detectMultiScale(gray,1.9,20)
for (x,y,w,h) in smile:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),7)
cv.imwrite("Smile_dection.jpg",img)