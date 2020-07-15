import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/lena.jpg',0)

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

hist_equal=Histogram_Equalization(img)
res = np.hstack((img,hist_equal)) #stacking images side-by-side
cv2.imshow('Histogram equalized',res)
cv2.waitKey(0)