import cv2 as cv
import numpy as np

# reading input image
img = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/cameraman.png')

# finding min and max intensity values [0-255]
a=np.min(img)        
b=np.max(img)

# function for linear stretching
def linContrastStretching(img,a,b):
    g = np.round(((img-a)/(b-a)))
    return g

g=linContrastStretching(img,a,b)
cv.imshow('Contrast Image',g)
cv.waitKey(0)