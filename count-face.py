import cv2
face_cascade = cv2.CascadeClassifier(r"C:\Users\NITHISH\Desktop\Opencv\xml-file\haarcascade-frontalface-default.xml")
image = cv2.imread(r"C:\Users\NITHISH\Desktop\Opencv\image\group.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, 1.9,4)
print(f"Number of faces detected: {len(faces)}")
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 7)
cv2.imwrite('Face-Detection-count.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()