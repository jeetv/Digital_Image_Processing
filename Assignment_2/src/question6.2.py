#6.2
import numpy as np
import cv2 as cv
import math


def distance(x, y, i, j):
    return np.sqrt((x-i)**2 + (y-j)**2)


def gaussian(x, sigma):
    return (1.0 / (2 * math.pi * (sigma ** 2))) * np.exp(- (x ** 2) / (2 * sigma ** 2))


def apply_bilateral_filter(img, diameter, sigma_i, sigma_s):
    row = img.shape[0]
    col = img.shape[1]
    channel = img.shape[2]
    filtered_img = np.zeros((row,col,channel)).astype(np.uint8)
    for x in range(0,row):
        for y in range(0,col):
            
            r = diameter // 2
            filtered1,filtered2,filtered3 = 0,0,0
            w1,w2,w3 = 0,0,0
            neighbour_x=0
            neighbour_y=0
           
            for i in range(0,r):
                for j in range(0,r):
                    n_x = x + (r - i)
                    n_y = y + (r - j)
                    if n_x >= row:
                        n_x -= row
                    if n_y >= col:
                        n_y -= col

            g_i_1 = gaussian(img[n_x, n_y,0] - img[x, y,0], sigma_i)
            g_i_2 = gaussian(img[n_x, n_y,1] - img[x, y,1], sigma_i)
            g_i_3 = gaussian(img[n_x, n_y,2] - img[x, y,2], sigma_i)
            g_s = gaussian(distance(n_x, x, n_y, y), sigma_s)
            wt1 = g_i_1 * g_s
            wt2 = g_i_2 * g_s
            wt3 = g_i_3 * g_s
            filtered1 += (img[n_x, n_y,0] * wt1)
            filtered2 += (img[n_x, n_y,1] * wt2)
            filtered3 += (img[n_x, n_y,2] * wt3)
            w1 += wt1
            w2 += wt2
            w3 += wt3
            
            if w1 != 0.0 and w2!=0 and w3!=0:
                filtered1 = filtered1 / w1
                filtered2 = filtered2 / w2
                filtered3 = filtered3 / w3

            filtered_img[x, y,0] = round(filtered1)
            filtered_img[x, y,1] = round(filtered2)
            filtered_img[x, y,2] = round(filtered3)
            
    return filtered_img

sky = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/gt_sky.png')
noir = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/gt_noir.png')
filtered_image_Sky = apply_bilateral_filter(sky, 10, 24.0, 28.0)
cv.imshow("SKY.png", filtered_image_Sky)

filtered_image_noir = apply_bilateral_filter(noir, 10, 24.0, 28.0)
cv.imshow("Noir.png", filtered_image_noir)
cv.waitKey(0)
