import cv2 as cv
import numpy as np

# reading input image
img = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/lena.jpg')

# function for Quantized Image
def BitQuantizeImage (img,k):
    g = np.array((np.floor(img/(2**(8-k))) * 255/(2**k-1)),dtype='uint8')
    return g

def NegativeImage(img,k,max_intensity):
    return max_intensity - (BitQuantizeImage(img,k))

g=NegativeImage(img,3,255)
cv.imshow('Negative Image',g)
cv.waitKey(0)