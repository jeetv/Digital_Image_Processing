# 1.3
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

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


def Prewitt(img):
    x_ker_p = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    y_ker_p = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    #Applying convolvution
    x_img_p = Convolve_Kernel(img,x_ker_p)
    y_img_p = Convolve_Kernel(img,y_ker_p)
    return x_img_p+y_img_p

def Sobel(img):
    x_kernel_s = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    y_kernel_s = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    #Applying convolvution
    x_img_s = Convolve_Kernel(img,x_kernel_s)
    y_img_s = Convolve_Kernel(img,y_kernel_s)
    return x_img_s+y_img_s
    
    

def Roberts(img):
    x_ker_r = np.array([[0,1],[-1,0]])
    y_ker_r = np.array([[1,0],[0,-1]])
    #Applying convolvution
    x_img_r = Convolve_Kernel(img,x_ker_r)
    y_img_r = Convolve_Kernel(img,y_ker_r)
    return x_img_r+y_img_r
    
    
def Laplacian(img):
    l_kernel1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    l_kernel2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    #Applying convolvution
    img_l_1 = Convolve_Kernel(img,l_kernel1)
    img_l_2 = Convolve_Kernel(img,l_kernel2)
    return img_l_1,img_l_2

img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/barbara.jpg',0)
mu, sigma = 0,10
noise = np.random.normal(mu, sigma, [img.shape[0],img.shape[1]])
noisy_img= (img+noise).astype(np.uint8)
cv.imwrite('Noisy Image.jpg',noisy_img)


p=Prewitt(noisy_img)
cv.imwrite('Prewitt_Noisy.jpg',p)


s=Sobel(noisy_img)
cv.imwrite('Sobel_Noisy.jpg',s)

r=Roberts(noisy_img)
cv.imwrite('Roberts_Noisy.jpg',r)

l1,l2=Laplacian(noisy_img)
cv.imwrite('Laplacian 1_Noisy.jpg',l1)
cv.imwrite('Laplacian 2_Noisy.jpg',l2)



# all gradient based (first order derivative) edge detections such as prewitt,sobel,roberts and canny are sensitive to noise - 
# when the noise occur these operators have a tendency to assume it as a part of the edge and also sometimes it misses the true edges due to corruption of noise
# canny overcomes this problem by applying gaussian filter on noisy image whoch reduces nosie to great extent.
# roberts yield the worst on noise and canny gives very good output 
    
# Laplacian (is second order derivative)
#the laplacian edge detector is extremely sensitive to noise. 
#Usually, you'll want to reduce noise - maybe using the Gaussian blur
#Laplacians are computationally faster to calculate (only one kernel vs two kernels that in gradient based)