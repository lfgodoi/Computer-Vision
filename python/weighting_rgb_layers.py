#
# Weighting RGB Layers
#
# Setting different proportions for the RGB layers (red, green and blue) of an image.
#
# Leonardo Franco de Godói
#
 
#------------------------------------------------------------------------------

# Importing package for computer vision with Python
import cv2 as cv           

# Importing package for scientific computing with Python
import numpy as np     

# Importing the image to be processed
img = cv.imread('C:/Users/leonardo/Desktop/img.jpg', 1) 

# Creating images 1, 2 and 3 from the original (also resizing) 
img_1 = cv.resize(img, (0, 0), fx=0.25, fy=0.25) 
img_2 = cv.resize(img, (0, 0), fx=0.25, fy=0.25) 
img_3 = cv.resize(img, (0, 0), fx=0.25, fy=0.25) 
 
# Weighting every layer and generating grayscale version of the image 1 
img_1[:, :, 2] = img_1[:, :, 2] * 0.15              # R weighting       
img_1[:, :, 1] = img_1[:, :, 1] * 0.55              # G weighting 
img_1[:, :, 0] = img_1[:, :, 0] * 0.3               # B weighting
img_1_gs = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)    # Grayscale 
 
# Weighting every layer and generating grayscale version of the image 2 
img_2[:, :, 2] = img_2[:, :, 2] * 0.3               # R weighting       
img_2[:, :, 1] = img_2[:, :, 1] * 0.15              # G weighting
img_2[:, :, 0] = img_2[:, :, 0] * 0.55              # B weighting 
img_2_gs = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)    # Grayscale 

# Weighting every layer and generating grayscale version of the image 3 
img_3[:, :, 2] = img_3[:, :, 2] * 0.55              # R weighting     
img_3[:, :, 1] = img_3[:, :, 1] * 0.3               # G weighting 
img_3[:, :, 0] = img_3[:, :, 0] * 0.15              # B weighting 
img_3_gs = cv.cvtColor(img_3, cv.COLOR_BGR2GRAY)    # Grayscale
 
# Saving resulting images 
cv.imwrite('C:/Users/leonardo/Desktop/img_1.jpg', img_1)
cv.imwrite('C:/Users/leonardo/Desktop/img_1_gs.jpg', img_1_gs) 
cv.imwrite('C:/Users/leonardo/Desktop/img_2.jpg', img_2)
cv.imwrite('C:/Users/leonardo/Desktop/img_2_gs.jpg', img_2_gs) 
cv.imwrite('C:/Users/leonardo/Desktop/img_3.jpg', img_3) 
cv.imwrite('C:/Users/leonardo/Desktop/img_3_gs.jpg', img_3_gs)
