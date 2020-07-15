# 5.1
import numpy as np 
import cv2 as cv


def Averaging_filter(img, kernel,k): 
   
    rows = img.shape[0]
    cols = img.shape[1]
    row_k,col_k = kernel.shape
    new_img= np.zeros((rows,cols)).astype(np.uint8)
    center = int(row_k/2)
   
    for x in range(0,rows-row_k):
        for y in range(0,cols-col_k):
            sum =0
            for i in range(0,row_k):
                for j in range(0,col_k):
                    sum = sum + kernel[i,j]*img[i+x,j+y]               
            #print(x+center,y+center)       
            new_img[x+center,y+center]= np.absolute(sum/k)  
           
    return new_img

img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/barbara.jpg',0)
kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])

# Using Linear filter(Average Filter)
filtered = Averaging_filter(img,kernel,9)
cv.imwrite('Linear_Filter.jpg',filtered)

