# 3.3

import numpy as np 
import cv2 as cv

# function for convolution with kernel
def Convolve_Kernel(img, kernel): 
    rows,cols=img.shape
    row_k,col_k = kernel.shape
    new_img= np.zeros((rows,cols)).astype(np.uint8)
    center = int(row_k/2)
    for x in range(0,rows-row_k):
        for y in range(0,cols-col_k):
            sum = 0
            for i in range(0,row_k):
                for j in range(0,col_k):
                    sum = sum + kernel[i,j]*img[i+x,j+y]
            #print(x+center,y+center)       
            new_img[x+center,y+center]= np.absolute(sum)   
    return new_img


img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/bell.jpg',0)
img=cv.resize(img,(512,512))

kernel = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernel_transpose = np.array([[1,1,-1],[1,0,-1],[1,-1,-1]])
#Applying convolvution
x_img = Convolve_Kernel(img,kernel)
y_img = Convolve_Kernel(img,kernel_transpose)
final = cv.hconcat([x_img,y_img])
cv.imshow('Blur.JPG Comaprison with Transpose Matrix',final)
cv.waitKey(0)  