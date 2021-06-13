# Import the libraries
import numpy as np
import cv2

# Read the image
nimg = 'image1' # Change 'image1' for the name of your image
imgray = cv2.imread(nimg + '.jpg', cv2.IMREAD_GRAYSCALE)
# Apply the threshold
nthresh = 'otsu'
t, dst = cv2.threshold(imgray, 0, 255, cv2.THRESH_OTSU)
# Show the image in gray scale
cv2.imshow('Gray scale', imgray)
# Show the image with the threshold
cv2.imshow('Threshold', dst)
cv2.imwrite(nimg + '_' + nthresh + '.png', dst)
# Wait until the user press a key
cv2.waitKey(0)
