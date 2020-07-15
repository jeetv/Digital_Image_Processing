import numpy as np
import cv2 as cv
# Read the image in greyscale
img = cv.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/cameraman.png',0)


#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
arr = []
rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
         arr.append(np.binary_repr(img[i][j] ,width=8)) # width = no. of bits

# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
bit8 = (np.array([int(i[0]) for i in arr],dtype = np.uint8)*128).reshape(rows,cols)
bit7= (np.array([int(i[1]) for i in arr],dtype = np.uint8)*64).reshape(rows,cols)
bit6 = (np.array([int(i[2]) for i in arr],dtype = np.uint8)*32).reshape(rows,cols)
bit5 = (np.array([int(i[3]) for i in arr],dtype = np.uint8)*16).reshape(rows,cols)
bit4 = (np.array([int(i[4]) for i in arr],dtype = np.uint8)*8).reshape(rows,cols)
bit3 = (np.array([int(i[5]) for i in arr],dtype = np.uint8)*4).reshape(rows,cols)
bit2 = (np.array([int(i[6]) for i in arr],dtype = np.uint8)*2).reshape(rows,cols)
bit1 = (np.array([int(i[7]) for i in arr],dtype = np.uint8)*1).reshape(rows,cols)


# horizontally concatenate
final = cv.hconcat([bit8,bit7,bit6,bit5,bit4,bit3,bit2,bit1])

# Display the images
cv.imshow('Bit Slicing',final)
cv.waitKey(0) 