# Import the libraries
import cv2


# Read the image
image = cv2.imread('image1.png', 1) # Change 'image1.png' for the name of your image
# See the original picture
cv2.imshow('Image 1', image)
# Set the time to see the image 
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
# Obtain the dimentions of the image
dimensions = image.shape
height = image.shape[0]
width = image.shape[1]
print('Height of the image: ' + str(height))
print('Width: ' + str(width))
# Extract one part of the image
startRow = 101
endRow = 103
startCol = 201
endCol = 203
croppedImage = image[startRow:endRow, startCol:endCol]
# Show the cropped image
cv2.imshow('Cropped image', croppedImage)
# Set the time to see the image 
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
