# 1.2
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

p=Prewitt(img)
cv.imwrite('Prewitt.jpg',p)
#cv.waitKey(0)

s=Sobel(img)
cv.imwrite('Sobel.jpg',s)
#cv.waitKey(0)

r=Roberts(img)
cv.imwrite('Roberts.jpg',r)
#cv.waitKey(0)

l1,l2=Laplacian(img)
cv.imwrite('Laplacian 1.jpg',l1)
cv.imwrite('Laplacian 2.jpg',l2)
#cv.waitKey(0)

b = cv.Canny(img,50,250)
cv.imwrite('Canny.jpg',b)
