
import cv2
image1 = cv2.imread(r'C:\Users\NITHISH\Desktop\Opencv\image\sample1.jpg')
image2 = cv2.imread(r'C:\Users\NITHISH\Desktop\Opencv\image\sample2.jpg')
height, width= image1.shape[:2]

# Define the coordinates where you want to paste image1 onto image2
x_offset = 100  # X coordinate for the top-left corner of the pasted image
y_offset = 150  # Y coordinate for the top-left corner of the pasted image

# Calculate the coordinates for the region of interest (ROI) in image2
roi = image2[y_offset:y_offset+height, x_offset:x_offset+width]

# Perform the copy-paste operation
image2[y_offset:y_offset+height, x_offset:x_offset+width] = image1

# Display the result
cv2.imwrite('Pasted_Image.jpg', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
