import numpy as np
import cv2
# Load the image
img = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/gamma-corr.png')

def Gamma(img,gamma):
    g = np.array(255*(img/255)**gamma,dtype='uint8')
    return g

g_output0 = Gamma(img,0.9)
g_output1 = Gamma(img,1.0)
g_output2 = Gamma(img,2.2)
g_output3 = Gamma(img,3.5)
g_output4 = Gamma(img,4)
# Display the images in subplots
final_img = cv2.hconcat([g_output0,g_output1,g_output2,g_output3,g_output4])
cv2.imshow('Gamma-Transform',final_img)
cv2.waitKey(0)
