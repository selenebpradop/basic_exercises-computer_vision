# Import the libraries
import cv2
import numpy as np

# Read the image
image = cv2.imread('image1.png',1) # Change 'image1.png' for the name of your image
# Obtain the dimensions of the image
row = image.shape[0]
col = image.shape[1]
ch = image.shape[2]
# Show the original picture
cv2.imshow('Image 1', image)
# Set the time to see the image 
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
# Add noise to the image
mean = 0
var = 0.1
sigma = var**0.5
noisy = np.zeros((row,col,ch), np.uint8)
noise = cv2.randn(noisy, (mean), (sigma))
noisyimg = image + noise
# Show the image with noise
cv2.imshow('Image with noise', noisyimg)
# Set the time to see the image 
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
