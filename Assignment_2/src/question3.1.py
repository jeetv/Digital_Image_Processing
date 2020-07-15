# 3.1
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


img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/box.png',0)
kernel = np.array([[1,1,1],[1,0,-1],[-1,-1,-1]])
#Applying convolvution
new_img = Convolve_Kernel(img,kernel)
final = cv.hconcat([img,new_img])
cv.imshow('White Line',final)
cv.waitKey(0)  