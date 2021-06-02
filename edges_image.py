# Import the libraries
import cv2

# Read the image
image = cv2.imread('image1.png',1) # Change 'image1.png' for the name of your image 
# Show the original image
cv2.imshow('Image 1', image)
# Set the time to show the image
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
# Detect the edges with Canny
edge_img = cv2.Canny(imagen,100,200)
# Show the image with the edges highlighted
cv2.imshow('Image with the edges highlighted', edge_img)
# Set the time to show the image
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
