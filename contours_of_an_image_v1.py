# Import the libraries
import numpy as np
import cv2

# Read the image
originalimage = cv2.imread("image1.png") # Change 'image1.png' for the name of your image

# Show the original picture
cv2.imshow("Original image", originalimage)
# Wait until the user press a key
cv2.waitKey(0)

# Convert the image to grayscale
grayimage = cv2.cvtColor(originalimage, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to the image
gauss = cv2.GaussianBlur(grayimage, (5,5), 0)

# Show the grayscale picture with the filter Gaussian Blur
cv2.imshow("Gaussian Blur", gauss)
cv2.waitKey(0)

# Detect the edges with Canny
canny = cv2.Canny(gauss, 50, 150)

# Show the image with the edges detected
cv2.imshow("Canny", canny)
cv2.waitKey(0)

# Count the number of edges
(contours, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Show the number of edges finded in the console
print("I find {} objets".format(len(contours)))

# Draw the edges in the original picture
cv2.drawContours(originalimage, contours, -1, (0,0,255), 2)
# Show the original image with the edges drawn
cv2.imshow("Contours", originalimage)
# Wait until the user press a key
cv2.waitKey(0)
