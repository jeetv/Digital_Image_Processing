import numpy as np
import cv2
import matplotlib.pyplot as plt

def cumulative_histogram(hist):
    cum_hist = np.copy(hist)
    
    for i in range(1, 256):
        cum_hist[i] = cum_hist[i-1] + cum_hist[i]
        
    return cum_hist

def histogram(img):
    height = img.shape[0]
    width = img.shape[1]
    
    hist = np.zeros((256))

    for i in range(height):
        for j in range(width):
            a = img[i,j]
            hist[a] += 1
    return hist

def Histogram_plot(title,img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    
    # plotting histogram
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.title(title)
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

img = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/eye.png', cv2.IMREAD_GRAYSCALE)
img_ref = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/eye.png', cv2.IMREAD_GRAYSCALE)

def Histogram_Matching(img,img_ref):
    Histogram_plot('Image',img)
    Histogram_plot('Ref Image',img_ref)
    row = img.shape[0]
    col = img.shape[1]
    pixels = row * col 
    pixels_ref = img_ref.shape[0] * img_ref.shape[1]

    hist = histogram(img)
    hist_ref = histogram(img_ref)

    cum_hist = cumulative_histogram(hist)
    cum_hist_ref = cumulative_histogram(hist_ref)

    prob_cum_hist = cum_hist / pixels

    prob_cum_hist_ref = cum_hist_ref / pixels_ref

    K = 256
    new_values = np.zeros((K))

    for a in range(K):
        j = K - 1
        while True:
            new_values[a] = j
            j = j - 1
            if j < 0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
                break

    for i in range(row):
        for j in range(col):
            a = img[i,j]
            b = new_values[a]
            img[i,j]=b
    return img

Hist_match=Histogram_Matching(img,img_ref)
Histogram_plot('Histogram Matched',Hist_match)
cv2.imshow('Histogram matched',Hist_match)
cv2.waitKey(0)
cv2.destroyAllWindows()




