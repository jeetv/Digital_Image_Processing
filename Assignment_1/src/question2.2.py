
import cv2
import numpy as np
from sklearn.cluster import KMeans


def make_histogram(cluster):
  
    numLabels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    hist, _ = np.histogram(cluster.labels_, bins=numLabels)
    hist = hist.astype('float32')
    hist /= hist.sum()
    return hist


def make_bar(height, width, color):
    
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)




img = cv2.imread('D:/DIP/Assignment_1/a1_2019701006/input_data/color_image.jpg')
height, width, _ = np.shape(img)


image = img.reshape((height * width, 3))


num_clusters = 4
clusters = KMeans(n_clusters=num_clusters)
clusters.fit(image)
histogram = make_histogram(clusters)
combined = zip(histogram, clusters.cluster_centers_)
combined = sorted(combined, key=lambda x: x[0], reverse=True)
bars = []
for index, rows in enumerate(combined):
    bar, rgb = make_bar(100, 100, rows[1])
    print(f'Bar {index + 1}')
    print(f'  RGB values: {rgb}')
    bars.append(bar)

cv2.imshow(f'{num_clusters} Most Frequent Occurring Color', np.hstack(bars))
cv2.waitKey(0)


