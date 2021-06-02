# Import the libraries
import cv2

# Read the image
imagen = cv2.imread('gatito.png',1)
# Show the original image
cv2.imshow('Imagen original', imagen)
# Set the time to show the image
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
# Detect the edges with Canny
edge_img = cv2.Canny(imagen,100,200)
# Show the image with the edges highlighted
cv2.imshow('Imagen con bordes resaltados', edge_img)
# Set the time to show the image
cv2.waitKey(10000)
# Close the image
cv2.destroyAllWindows()
