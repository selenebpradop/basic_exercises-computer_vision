# Import the libraries
import cv2
import numpy as np

# Read the image
image = cv2.imread('image1.png') # Change 'image1.png' for the name of your image
# Apply middle filter 3x3 in the image
kernel = np.ones((3,3),np.float32)/9
processed_image = cv2.filter2D(image, -1, kernel)
# Show the original picture
cv2.imshow('Original image', image)
# Wait until the user press a key
cv2.waitKey(0)
# Show the image with the filter
cv2.imshow('Middle filter 3x3 in the image', processed_image)
# Wait until the user press a key
cv2.waitKey(0)
