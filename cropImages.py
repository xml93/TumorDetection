import cv2
import numpy as np
from matplotlib import pyplot as plt

def plot():
    start = (startX, startY)
    end = (endX, endY)
    cv2.rectangle(img,start, end, 255, 2)
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.show()

img=cv2.imread('1.jpeg')
height, width, channels = img.shape
startX = width//2
startY = height//2
endX = 0
endY = height//2
for y in range(height):
    for x in range(width):
        if img[y][x][0] > 30 or img[y][x][1] > 30 or img[y][x][2] > 30:
            if startY > y:
                startY = y
                print(str(img[x][y][0]))
                print(str(img[x][y][1]))
                print(str(img[x][y][2]))
                print("___")
            if startX > x:
                startX = x
            if endX < x:
                endX = x
            if endY < y:
                endY = y
            #print(str(x) + ":" + str(y))
            #print(str(img[x][y]))
print("X:" + str(startX))
print("Y:" + str(startY))
plot()
