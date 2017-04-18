import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('1.jpeg')
height, width, channels = img.shape
startX = width//2
startY = 0
endX = 0
endY = height//2
for x in range(width):
    for y in range(height):
        if img[x][y][0] > 100 or img[x][y][1] > 100 or img[x][y][2] > 100:
            if startY == 0:
                startY=y
            if startX > x:
                startY = x
            if endX < x:
                endX = x
            if endY > y:
                endY = y
            #print(str(x) + ":" + str(y))
            #print(str(img[x][y]))

start = (startX, startY)
end = (endX, endY)
cv2.rectangle(img,start, end, 255, 2)
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.show()
