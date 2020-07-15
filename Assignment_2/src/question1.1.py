# 1.1
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

bell = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/bell.jpg')
cube = cv.imread('D:/DIP/Assignment_2/a2_2019701006/input_data/cubes.png')
edges_bell = cv.Canny(bell,50,250)
edges_cube = cv.Canny(cube,50,150)

plt.subplot(121),plt.imshow(edges_bell,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(edges_cube,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()