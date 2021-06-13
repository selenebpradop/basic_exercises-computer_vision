# Import the libraries
import cv2
import numpy as np
import math as m
from matplotlib import pyplot as plt

#-- PRE-PROCESSING --
# Read the image
nimg = 'image1' # Change 'image1' for the name of your image
image = cv2.imread(nimg + '.jpg')
# Extract the RGB layers of the image
rgB = np.matrix(image[:,:,0]) # Blue
rGb = np.matrix(image[:,:,1]) # Green
Rgb = np.matrix(image[:,:,2]) # Red
# Define the combination RGB
II = cv2.absdiff(rGb,rgB)
I = II*255
cv2.imshow('Images with layers extracted', I)
cv2.waitKey(0)
# Initial binarization of the image
[fil, col] = I.shape
for o in range(0,fil):
    for oo in range(0,col):
        if I[o, oo]<80:      # Pixel less than 80 will be 0
            I[o,oo]=0
for o in range(0,fil):
    for oo in range(0,col):
        if I[o, oo]>0:       # Pixel more than 0 will be 1 
            I[o,oo]=1
# Morphological transformations
# Create square streel: se for closing and se2 for dilation
se = np.ones((50, 50), np.uint8)
se2 = np.ones((10, 10), np.uint8)
closing = cv2.morphologyEx(I,cv2.MORPH_CLOSE,se) # Closing
dilation = cv2.dilate(closing,se2,1)             # Dilation
# Find the contours
contours,hierarchy=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# Extract the contours
cnt = contours[:]
num = len(cnt)
# print(num)
# print(contours)
# print(hierarchy)
# Calculate the bigger contour
box = np.zeros((num,4))
for j in range(0, num):
    box[j,:]=cv2.boundingRect(cnt[j])
L = np.zeros((num,4))
Max=[0,0]    
for j in range(0, num):   
    L[j,:]=box[j]         
    if L[j,2]>Max[1]:     
        Max=[j,L[j,2]]
BOX = box[Max[0],:]
# Mask
b = image[int(BOX[1]):int(BOX[1]+BOX[3]),int(BOX[0]):int(BOX[0]+BOX[2]),:]

#-- SEGMENTATION --
[fil,col,cap] = b.shape
# Extract the RGB layers of the image with the mask
rgB = b[:,:,0] # Blue
rGb = b[:,:,1] # Green
Rgb = b[:,:,2] # Red
# Normalizate the layers
R = Rgb/255.0
G = rGb/255.0
B = rgB/255.0
# Build the color K space
K = np.zeros((fil,col))                    # Black layer
for o in range(0,fil):
    for oo in range(0,col):
        MAX = max(R[o,oo],G[o,oo],B[o,oo]) # Calculate the maximum value R-G-B
        K[o,oo] = 1-MAX
# Save the image in .bmp format
cv2.imwrite('imgbmp_' + nimg + '.bmp', K)
# Read the image
k = cv2.imread('imgbmp_' + nimg + '.bmp')
# Apply Canny
BW1 = cv2.Laplacian(k, cv2.CV_8UC1)
# Extract layers
imgk = BW1[:,:,0]+BW1[:,:,1]+BW1[:,:,2]
# Save the image
cv2.imwrite('result_' + nimg + '.png', imgk*255)
