import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/lena.jpg',0)
img2 = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/cameraman.png',0)
img3 = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/gamma-corr.png',0)

img1 = cv.resize(img1,(256,256))
img2= cv.resize(img2,(256,256))
img3= cv.resize(img3,(256,256))
#function for histogram equaliztion
def Histogram_Equalization(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    
    # plotting histogram for original image
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.title('Original Image Histogram ')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

    # calcuation of histogram equalization
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img2 = cdf[img]
    
    #plotting histogram equalized image
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img2.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.title('Histogram Equalization')
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()
    return img2

hist_equal1=Histogram_Equalization(img1)
hist_equal2=Histogram_Equalization(img2)
hist_equal3=Histogram_Equalization(img3)
res1 = np.hstack((img1,hist_equal1))
res2 = np.hstack((img2,hist_equal2))
res3 = np.hstack((img3,hist_equal3))
final= cv2.vconcat([res1,res2,res3])#stacking images side-by-side
cv2.imshow('Histogram equalized',final)
cv2.waitKey(0)