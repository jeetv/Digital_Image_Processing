# 5.3
import numpy as np 
import cv2 as cv
import time

def Median_Filter_own(img, k):
    start = time.time()
    rows = img.shape[0]
    cols = img.shape[1]
    row_k = k
    col_k = k
    new_img= img
   
    #center = int(row_k/2)
    for x in range(0,rows-row_k):
        for y in range(0,cols-col_k):
            window=[]
            for i in range(0,row_k):
                for j in range(0,col_k):
                    window = np.append(window,(img[i+x,j+y]))
                    
                  
            #print(x+center,y+center)       
            new_img[x,y]= np.median(window)   
    time_taken=time.time()-start        
    return new_img,time_taken

def plott(x,y1,y2,l,l1):
    plt.xlim(3,5,9)
    plt.plot(x,y1,label=l1, linestyle='dashed')
    plt.plot(x,y2,label=l, linestyle='dashed')
    plt.xlabel('K')
    plt.ylabel('Run Time (in msecs)')
    plt.legend(loc="upper left")
    plt.xticks(np.arange(1, 9, 2))
    plt.show()

img = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/Degraded.jpg', 0)

# Using Efficient Average Filter
img1=np.resize(img,(256,256))
x = [3,5]
filtered1,time1 = Median_Filter_own(img1,3)
filtered2,time2 = Median_Filter_own(img1,5)
y1 = [time1,time2]

filtered1,time1 = Median_Filter_own(img,3)
filtered2,time2 = Median_Filter_own(img,5)
y2 = [time1,time2]
plott(x,y1,y2,img.shape,img1.shape)
