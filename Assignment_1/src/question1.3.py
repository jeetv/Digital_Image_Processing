# Write a function mergeImage which takes two images fg and bg that extracts the foreground object and places it in the background and returns the resultant image.

import numpy as np
import cv2 as cv
fgimg = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/fg.jpg')
bgimg = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/canyon.png')

fgimg = cv.resize(fgimg,(256,256))
bgimg= cv.resize(bgimg,(256,256))
rows,cols,_=np.shape(fgimg)

#function to merge fg and bg
def ImageMerge(fgimg,bgimg):
    a=np.zeros((256,256,256))
    for i in range(rows):
        for j in range(cols):
            blue,green,red = fgimg[i][j]
            a[blue][green][red]+=1
        
    result = np.where(a == np.amax(a))
    listOfCordinates = np.reshape(result,(1,3))
   
    for i in range(rows):
        for j in range(cols):
            for k in range(0,3):
                if (fgimg[i][j][k]==listOfCordinates[0][k]):
                    fgimg[i][j][k]= 255

    for i in range(rows):
        for j in range(cols):
            for k in range(0,3):
                if (fgimg[i][j][k]==255):
                    fgimg[i][j][k]= bgimg[i][j][k]          
    return fgimg

merged_image = ImageMerge(fgimg,bgimg)
cv.imshow('Merging Image',merged_image) 
cv.waitKey(0)