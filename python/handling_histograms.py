'''

TITLE: 
   Handling Image Histograms (Simple and Cumulative)

DESCRIPTION:
   Use of the main OpenCV histogram features, emphasizing the 
   possibility of generating the simple and accumulated graphs
   
VERSION: 
   Author: Leonardo Godói (eng.leonardogodoi@gmail.com)
   Creation date: 14-September-2018

REVISION HISTORY:
   V1.0 | 14-September-2018 | Leonardo Godói | Creation

'''

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

# Importing package for computer vision with Python
import cv2 as cv           

# Importing package for scientific computing with Python
import numpy as np   
     
# Importing package for plotting graphics	 
from matplotlib import pyplot as plt   

# Importing the image in grayscale to be processed and resizing it 
img = cv.imread('imgs/messi.jpg', 0) 
img_original = cv.resize(img, (0, 0), fx=0.5, fy=0.5) 
 
# Applying equalization in the histogram
img_equalized = cv.equalizeHist(img_original)

# Plotting before and after graphics of histogram
plt.hist(img_original.ravel(),256,[0,256], color='red', label='Original') 
plt.legend() 
plt.show() 
plt.hist(img_equalized.ravel(),256,[0,256], color='green', label='equalizada')  
plt.legend() 
plt.show() 
 
# Plotting before and after graphics of cumulative histogram 
plt.hist(img_original.ravel(),256,[0,256], color='red', label='Original', cumulative=True) 
plt.legend() 
plt.show() 
plt.hist(img_equalized.ravel(),256,[0,256], color='green', label='equalizada', cumulative=True)  
plt.legend() 
plt.show() 
 
# Saving original and equalized images side by side for comparison
img_original_equalized = np.hstack((img_original, img_equalized)) 
cv.imwrite('imgs/messi_original_equalized.jpg', img_original_equalized) 

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------