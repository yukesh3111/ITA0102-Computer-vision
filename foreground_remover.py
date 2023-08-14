import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

segmentor = SelfiSegmentation()

# read image
imgOffice = cv2.imread(r'C:\Users\NITHISH\Desktop\Opencv\image\person.jpg')

#resize office to 640x480
imgOffice = cv2.resize(imgOffice, (640, 480))

green = (0, 255, 0)

imgNoBg = segmentor.removeFG(imgOffice, green, threshold=0.50)

# show both images
cv2.imshow('office',imgOffice)
cv2.imwrite('Foreground_remover.jpg',imgNoBg)


cv2.waitKey(0)
cv2.destroyAllWindows()