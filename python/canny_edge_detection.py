'''

TITLE: 
   Canny Edge Detection

DESCRIPTION:
   Use of the Canny algorithm for edge detection in an image.
   
VERSION: 
   Author: Leonardo Godói (eng.leonardogodoi@gmail.com)
   Creation date: 11-September-2018

REVISION HISTORY:
   V1.0 | 11-September-2018 | Leonardo Godói | Creation

'''

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

# Importing package for computer vision with Python
import cv2 as cv           

# Importing package for scientific computing with Python
import numpy as np   

# Importing the image in grayscale to be processed and resizing it 
img = cv.imread('imgs/messi.jpg', 0)  
img_or = cv.resize(img, (0, 0), fx=0.5, fy=0.5) 
 
# Creating a pre-smoothed image by using a gaussian filter
img_bl = cv.GaussianBlur(img_or,(5,5),0) 
 
# Applying the Canny algorithm for detecting edges on both original and smoothed images
img_original_edges = cv.Canny(img_or, 100, 200) 
img_blurred_edges = cv.Canny(img_bl, 100, 200) 
 
# Saving the images processed by the algorithm side by side for comparison 
img_or_ed = np.hstack((img_or,img_original_edges)) 
img_bl_ed = np.hstack((img_bl,img_blurred_edges)) 
cv.imwrite('imgs/messi_original_edges.jpg', img_original_edges) 
cv.imwrite('imgs/messi_blurred_edges.jpg', img_blurred_edges)

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------