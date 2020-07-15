# 8
import numpy as np 
import cv2 as cv

def Median_Filter_own(img, k): 
    rows = img.shape[0]
    cols = img.shape[1]
    row_k = k
    col_k = k
    new_img= img
   
    #center = int(row_k/2)
    for x in range(0,rows-row_k):
        for y in range(0,cols-col_k):
            window1=[]
            window2=[]
            window3=[]
            for i in range(0,row_k):
                for j in range(0,col_k):
                    window1 = np.append(window1,(img[i+x,j+y,0]))
                    window2 = np.append(window2,(img[i+x,j+y,1]))
                    window3 = np.append(window3,(img[i+x,j+y,2]))
            #print(x+center,y+center)       
            new_img[x,y,0]= np.median(window1) 
            new_img[x,y,1]= np.median(window2) 
            new_img[x,y,2]= np.median(window3) 
    return new_img

img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/Degraded.jpg')
img1=img
clear_image = Median_Filter_own(img,3)
cv.imshow('Original Image',img1)
cv.imshow('Clear Image',clear_image)
cv.waitKey(0)