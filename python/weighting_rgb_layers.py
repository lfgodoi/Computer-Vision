'''

TITLE: 
   Weighting and Splitting RGB Layers

DESCRIPTION:
   Setting different proportions for the RGB layers (red, green 
   and blue) of an image and splitting it up.
   
VERSION: 
   Author: Leonardo Godói (eng.leonardogodoi@gmail.com)
   Creation date: 15-September-2018

REVISION HISTORY:
   V1.0 | 15-September-2018 | Leonardo Godói | Creation

'''

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

# Importing package for computer vision with Python
import cv2 as cv             

# Importing the image to be processed
img = cv.imread('imgs/messi.jpg', 1) 

# Creating images 1, 2 and 3 from the original (also resizing) 
img_1 = cv.resize(img, (0, 0), fx=0.25, fy=0.25) 
img_2 = cv.resize(img, (0, 0), fx=0.25, fy=0.25) 
img_3 = cv.resize(img, (0, 0), fx=0.25, fy=0.25) 
 
# Weighting every layer of the image 1 
img_1[:, :, 2] = img_1[:, :, 2] * 0.15              # R weighting       
img_1[:, :, 1] = img_1[:, :, 1] * 0.55              # G weighting 
img_1[:, :, 0] = img_1[:, :, 0] * 0.3               # B weighting
 
# Weighting every layer of the image 2 
img_2[:, :, 2] = img_2[:, :, 2] * 0.3               # R weighting       
img_2[:, :, 1] = img_2[:, :, 1] * 0.15              # G weighting
img_2[:, :, 0] = img_2[:, :, 0] * 0.55              # B weighting 

# Weighting every layer of the image 3 
img_3[:, :, 2] = img_3[:, :, 2] * 0.55              # R weighting     
img_3[:, :, 1] = img_3[:, :, 1] * 0.3               # G weighting 
img_3[:, :, 0] = img_3[:, :, 0] * 0.15              # B weighting 
 
# Saving resulting images 
cv.imwrite('imgs/img_1.jpg', img_1)
cv.imwrite('imgs/img_2.jpg', img_2)
cv.imwrite('imgs/img_3.jpg', img_3) 

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------