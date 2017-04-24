import cv2
import numpy as np
from matplotlib import pyplot as plt
from cropImages import crop

def getImageBrigthness(img):
    height, width, channels = img.shape
    total = 0
    r=0
    g=0
    b=0
    count = 0
    for y in range(height):
        for x in range(width):
            total += (img[y][x][0] + img[y][x][1] + img[y][x][2])//3
            r += img[y][x][0]
            g += img[y][x][1]
            b += img[y][x][2]
            count = count + 1
    return total//count, r//count, g//count, b//count

def main():
    maxId = 10
    crop(maxId)
    imgcodes = range(1,maxId)
    for imgcode in imgcodes:
        fileName = "new_" + str(imgcode) + '.jpeg'
        img = cv2.imread(fileName)
        print(str(getImageBrigthness(img)))
        img2 = img.copy()
        template = cv2.imread('template.jpeg')
        w, h, c = template.shape
        
        templateSizingSteps = np.arange(0.9,1.3,0.1)
        for step in templateSizingSteps:
            print("Current resizing step: " + str(step))
            height, width = template.shape[:2]
            template = cv2.resize(template,(int(height*step), int(width*step)), interpolation = cv2.INTER_CUBIC)
            print(str(template.shape[:2]))
            # All the 6 methods for comparison in a list
#            methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#                        'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

            methods = ['cv2.TM_SQDIFF_NORMED']
            for meth in methods:
                print
                img = img2.copy()
                method = eval(meth)

                # Apply template Matching
                res = cv2.matchTemplate(img,template,method)

                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                print("max_val" + str(max_val))
                print("min_loc" + str(min_loc))
                print("max_loc" + str(max_loc))
                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)

                cv2.rectangle(img,top_left, bottom_right, 255, 2)
                plt.subplot(121),plt.imshow(res,cmap = 'gray')
                plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                plt.subplot(122),plt.imshow(img,cmap = 'gray')
                plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                plt.suptitle(meth)

                plt.show()

main()
