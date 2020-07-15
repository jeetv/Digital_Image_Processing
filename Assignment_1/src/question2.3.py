import cv2 as cv
import numpy as np

# reading input image
img1 = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/lena.jpg')
img2 = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/cameraman.png')
img3 = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/gamma-corr.png')


img1 = cv.resize(img1,(256,256))
img2= cv.resize(img2,(256,256))
img3= cv.resize(img3,(256,256))


# function for linear stretching
def linContrastStretching(img,a,b):
    g = np.round(((img-a)/(b-a)))
    return g

g1=linContrastStretching(img1,np.min(img1),np.max(img1))
g2=linContrastStretching(img2,np.min(img2),np.max(img2))
g3=linContrastStretching(img3,np.min(img3),np.max(img3))
final = cv.hconcat([g1,g2,g3])

cv.imshow('Contrast Image',final)
cv.waitKey(0)