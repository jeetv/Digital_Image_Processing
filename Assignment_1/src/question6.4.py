import numpy as np
import cv2 as cv

p1=cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/part1.png',0)
p2=cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/part2.png',0)
p3=cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/part3.png',0)
p4=cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/part4.png',0)

img1 = cv.resize(p1,(256,256))
img2= cv.resize(p2,(256,256))
img3= cv.resize(p3,(256,256))
img4= cv.resize(p4,(256,256))
i = cv.hconcat([img1,img2])
j = cv.hconcat([img3,img4])
final=cv.vconcat([i,j])

#cv.imshow('image',final)

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


img_ref = cv.imread('D:\DIP\Assignment_1\A1_resources\DIP_2019_A1\canyon.png', 0)

def Histogram_Matching(img,img_ref):
    
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

def Histogram_Equalization(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    
    #plotting Combined image
    Histogram_plot('Original',img)

    # calcuation of histogram equalization
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img2 = cdf[img]
    
    return img2

equal = Histogram_Equalization(final)
Hist_match=Histogram_Matching(equal,img_ref)
Histogram_plot('Merged Image',Hist_match)
cv.imshow('Merged Image',Hist_match)
cv.waitKey(0)
#cv.destroyAllWindows()