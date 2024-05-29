#find edge image of f

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lena.png', 0)
img1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows,cols = img1.shape
prewitt_x = np.array([[1,1,1],[0,0,0],[-1,-1,1]]) 
prewitt_y= np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

def  
