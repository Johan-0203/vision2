import numpy as np
import cv2 as cv
import math

W = 500
H = 500

def show_im(im):
    cv.imshow('window',im)
    cv.waitKey(0)

def draw(triangle, im, color=(0,255,0)):
    cv.drawContours(im, [triangle.astype(int)], 0, color, -1)

def tras(triangle,dx,dy):
    t = np.array ((dx,dy))
    return triangle+t

def esc(triangle,x,y):
    e = np.array([(x,0),(0,y)])
    return triangle @ e

def rot(triangle):
    r = np.array([[np.cos(math.pi/2),-np.sin(math.pi/2)], [np.sin(math.pi/2), np.cos(math.pi/2)]])
    return triangle @ r


im = np.zeros((W,H,3))
triangle = np.array ([(10,10),(70,10),(40,60)])
# draw(triangle, im)
# show_im(im)
t1 = tras(triangle, 50,50)
# draw(t1,im, color=(0,0,255))
# show_im(im)
t2 = esc(t1,3,3)
# draw(t2,im, color=(255,0,0))
# show_im(im)
t3 = rot(t2)
draw(t3,im, color=(123,23,75))
show_im(im)