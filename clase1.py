"""
Ejercicio de clase 1: Introducción

JACG
"""

import cv2 as cv
import numpy as np
import math

S = 100

def img_1():
    im = np.zeros((100,100))
    for i in range(S):
        im[i,i] = 255
        cv.imwrite('image1.jpg',im)
img_1()

def img_2():
    im = np.zeros((100,100,3))
    red= (0,0,255)
    green= (0,255,0)
    blue= (255,0,0)

    #-----FORMA 1-----
    rectangle = np.array([(25,25),(75,25),(75,75),(25,75)])
    cv.drawContours(im, [rectangle.astype(int)], 0, red, -1)
    rectangle = np.array([(31,31),(69,31),(69,69),(31,69)])
    cv.drawContours(im, [rectangle.astype(int)], 0, green, -1)
    rectangle = np.array([(37,37),(63,37),(63,63),(37,63)])
    cv.drawContours(im, [rectangle.astype(int)], 0, blue, -1)
    rectangle = np.array([(43,43),(57,43),(57,57),(43,57)])
    cv.drawContours(im, [rectangle.astype(int)], 0, (0,0,0), -1)

    #-----FORMA 2-----
    # im[25:75,25:75] = red
    # im[31:69,31:69] = green
    # im[37:63,37:63] = blue
    # im[43:57,43:57] = 0

    cv.imwrite('image2.jpg',im) #Borrosa
    # cv.imshow('image2.jpg',im) #Nitida
    # cv.waitKey(0)
img_2()

def img_3():
    im = np.zeros((100,100,3), np.uint8)
    func = lambda x: round(50 * math.sin(x*0.09) + 1)
    x,y = (0, 0)
    # for i in range(0,100,4):
    while x<100:
        y = func(x)
        im[y:y+2, round(x):round(x)+2] = (255, 0,0)
        
        x+=1
    cv.imwrite('image3.jpg', im)
    # cv.waitKey(0)

img_3()