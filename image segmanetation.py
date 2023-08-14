import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\NITHISH\Desktop\Opencv\image\person.jpg')

# Define the lower and upper bounds for the color you want to segment (in BGR format)
lower_bound = np.array([0, 0, 100])  # Example: Dark blue
upper_bound = np.array([100, 100, 255])  # Example: Light blue

# Create a mask based on the color bounds
mask = cv2.inRange(image, lower_bound, upper_bound)

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image, mask, and segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Color Mask', mask)
cv2.imwrite('Segmented Image.jpg', segmented_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
