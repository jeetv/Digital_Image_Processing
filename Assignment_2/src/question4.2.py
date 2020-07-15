# 4.1
import numpy as np 
import cv2 as cv

# function for convolution with kernel
def Blur_Img(img, kernel,k): 
    rows = img.shape[0]
    cols = img.shape[1]
    channel = img.shape[2]
    row_k,col_k = kernel.shape
    new_img= np.zeros((rows,cols,channel)).astype(np.uint8)
    center = int(row_k/2)
    for x in range(0,rows-row_k):
        for y in range(0,cols-col_k):
            sum1 = 0
            sum2 = 0
            sum3 = 0
            for i in range(0,row_k):
                for j in range(0,col_k):
                    sum1 = sum1 + kernel[i,j]*img[i+x,j+y,0]
                    sum2 = sum2 + kernel[i,j]*img[i+x,j+y,1]
                    sum3 = sum3 + kernel[i,j]*img[i+x,j+y,2]
            #print(x+center,y+center)       
            new_img[x+center,y+center,0]= np.absolute(sum1/k) 
            new_img[x+center,y+center,1]= np.absolute(sum2/k)
            new_img[x+center,y+center,2]= np.absolute(sum3/k)
    return new_img


img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/Clear.jpg')
img=cv.resize(img,(512,512))
img1=img
kernel1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
kernel2 = np.array([[1,4,6,4,1],[4,16,26,16,4],[6,26,43,26,6],[4,16,26,16,4],[1,4,6,4,1]])

blur_img1 = Blur_Img(img,kernel1,9)
blur_img2 = Blur_Img(img1,kernel2,256)
#img_mask = img - blur_img
k=2
#highboost_img = img + k*(img_mask)
highboost_img1 = (k+1)*img - k*(blur_img1)
highboost_img2 = (k+1)*img1 - k*(blur_img2)

cv.imshow('Original Image',img)
cv.imshow('Blur',blur_img)
cv.imshow('HighBoost Image 1',highboost_img1)
cv.imshow('HighBoost Image 2',highboost_img2)
cv.waitKey(0)  