#5.2
import numpy as np 
import cv2 as cv
import time
import matplotlib.pyplot as plt

# function for convolution with kernel
def Modified_Averaging_filter(img, kernel,k): 
    start = time.time()
    rows = img.shape[0]
    cols = img.shape[1]
    row_k,col_k = kernel.shape
    new_img= np.zeros((rows,cols)).astype(np.uint8)
    center = int(row_k/2)
    sum =0
    for x in range(0,rows-row_k):
        c=0
        for y in range(0,cols-col_k):
            sum = sum - c
            if(y==0):
                r=0
            else:
                r=1
            for i in range(0,row_k):
                for j in range(r,col_k):
                    if(j==0):
                        c = c + kernel[i,j]*img[i+x,j+y]    
                    sum = sum + kernel[i,j]*img[i+x,j+y]               
            #print(x+center,y+center)       
            new_img[x+center,y+center]= np.absolute(sum/k)  
    time_taken=time.time()-start       
    return new_img,time_taken

def Averaging_filter(img, kernel,k): 
    start = time.time()
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
    time_taken=time.time()-start       
    return new_img,time_taken

def plott(x,y,y1,y2,l,l1):
    plt.xlim(3,5,9)
    plt.plot(x,y,label=(l,'Default'))
    plt.plot(x,y1,label=(l,'Efficient'), linestyle='dashed')
    plt.plot(x,y2,label=(l1,'Efficient'), linestyle='dashed')
    plt.xlabel('K')
    plt.ylabel('Run Time (in msecs)')
    plt.legend(loc="upper left")
    plt.xticks(np.arange(1, 11, 2))
    plt.show()

img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/bell.jpg',0)


kernel1 = np.ones([3, 3], dtype = int) 
kernel2 = np.ones([5, 5], dtype = int) 
kernel3 = np.ones([7, 7], dtype = int) 

# Using Default Average Filter
filtered1,time1 = Averaging_filter(img,kernel1,9)
filtered2,time2 = Averaging_filter(img,kernel2,25)
filtered3,time3 = Averaging_filter(img,kernel3,49)
x = [kernel1.shape[0],kernel2.shape[0],kernel3.shape[0]]
y = [time1,time2,time3]


# Using Efficient Average Filter
img1=np.resize(img,(256,256))
filtered1,time1 = Modified_Averaging_filter(img,kernel1,9)
filtered2,time2 = Modified_Averaging_filter(img,kernel2,25)
filtered3,time3 = Modified_Averaging_filter(img,kernel3,49)
y1 = [time1,time2,time3]

filtered1,time1 = Modified_Averaging_filter(img1,kernel1,9)
filtered2,time2 = Modified_Averaging_filter(img1,kernel2,25)
filtered3,time3 = Modified_Averaging_filter(img1,kernel3,49)
y2 = [time1,time2,time3]


plott(x,y,y1,y2,img.shape,img1.shape)
  