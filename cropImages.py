import cv2
import numpy as np
from matplotlib import pyplot as plt

def plot():
    start = (startX, startY)
    end = (endX, endY)
    cv2.rectangle(img,start, end, 255, 2)
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.show()

def crop(fileName):
    img=cv2.imread(fileName)
    height, width, channels = img.shape
    startX = width//2
    startY = height//2
    endX = 0
    endY = height//2
    for y in range(height):
        for x in range(width):
            if img[y][x][0] > 50 or img[y][x][1] > 50 or img[y][x][2] > 50:
                if startY > y:
                    startY = y
                if startX > x:
                    startX = x
                if endX < x:
                    endX = x
                if endY < y:
                    endY = y

    cropped = img[startY:endY, startX:endX]
    fileName= "cropped_" + fileName
    cv2.imwrite(fileName,cropped)
    #plot()

def main(fileDir,fileName):
    crop(fileDir,fileName)

