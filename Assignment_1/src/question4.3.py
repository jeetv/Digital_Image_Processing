import numpy as np
import cv2 as cv

img=cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/lena.jpg',0)

def Piece_wise_func1(img,k1,k2,k3,a,b):
    row, col=np.shape(img)
    new_img=np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            if(img[i,j]<(a*255)):
                new_img[i][j]=0
            elif((img[i,j]==(a*255) or img[i,j]==(b*255))):
                new_img[i,j]= (0.4*img[i,j])
            elif(img[i,j]>=(a*255) and img[i,j]<=(0.6*255)):
                new_img[i,j] = k1*img[i,j]
            elif(img[i,j]<=(b*255) and img[i,j]>=(0.6*255)):
                 new_img[i,j] = k2*img[i,j] + k3
    return new_img

def Piece_wise_func2(img,a,b,c,d):
    row, col=np.shape(img)
    new_img=np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            if(img[i,j]==a*255 or img[i,j]==b*255 or img[i,j]==c*255 or img[i,j]==d*255 or img[i,j]==255):
                new_img[i,j]= img[i,j]
            elif(img[i,j]>a*255 and img[i,j]<b*255):
                new_img[i,j]=a
            elif(img[i,j]>b*255 and img[i,j]<c*255):
                new_img[i,j]=b   
            elif(img[i,j]>c*255 and img[i,j]<d*255):
                new_img[i,j]=c
            elif(img[i,j]>d*255 and img[i,j]<255):
                new_img[i,j]=d    
                
    return new_img



fun1=Piece_wise_func1(img,1.33333,-2,2,0.3,0.8)
fun2=Piece_wise_func2(img,0.2,0.4,0.6,0.8)
cv.imshow('Piece_wise transform function 1',fun1)
cv.imshow('Piece_wise transform function 2',fun2)
cv.waitKey(0)            
        