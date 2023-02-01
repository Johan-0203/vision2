"""
Ejercicio de clase 1: Introducción

JACG
"""

import cv2 as cv
import numpy as np

S = 100

def img_1():
    im = np.zeros((100,100))
    for i in range(S):
        im[i,i] = 255
        cv.imwrite('image1.jpg',im)
img_1()

def img_2():
    im = np.zeros((100,100))
    # im_rgb = cv.cvtColor(im, cv.COLOR_GRAY2BGR)
    for i in range(S):
        im[25:75,25:75] = 255
        im[35:65,35:65] = 0
        im[45:55,45:55] = 255
        cv.imwrite('image2.jpg',im)
img_2()