# 1. Write a function that takes a color image and ﬁnds the most frequently occurring color from the image

import numpy as np
import cv2 as cv
img = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/color_image.jpg')
rows,cols,_=np.shape(img)

#function to find most frequent color
def Most_Freq_Color(img):
    a=np.zeros((256,256,256))
    for i in range(rows):
        for j in range(cols):
            blue,green,red = img[i][j]
            a[blue][green][red]+=1
        
    result = np.where(a == np.amax(a))
    listOfCordinates = np.reshape(result,(1,3))
    return listOfCordinates


most_freq = np.zeros((rows,cols,3), np.uint8)
most_freq[:][:] = Most_Freq_Color(img)
final= np.hstack((img,most_freq))
#printing the pixel value
print('Most frequently ocurring Pixel Value (B,G,R):',most_freq[0][0])
# displaying the image input image on right and most frequent color on left
cv.imshow('Most frequent occurring color',final) 
cv.waitKey(0)