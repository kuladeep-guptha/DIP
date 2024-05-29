# convert lena image into gray scale image. Implement all Geometric Transformations on the grayscale image without using inbuilt functions. 
# The list of Geometric Transformations to be applied are as follows:
# (A) Translation
# (B) Scaling
# (C) Rotation
# (D) Shearing in X - direction
# (E) Shearing in Y - direction


import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

image = cv2.imread('Lena.png')

image1= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Translation
rows,cols = image1.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(image1,M,(cols,rows))
plt.imshow(dst, cmap='gray')
plt.show()


def translate(image,x,y):
    translated_image=np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if i+y<image.shape[0] and j+x<image.shape[1]:
                translated_image[i+y][j+x]=image[i][j]
    return translated_image
translated_image=translate(image1,100,50)


#scaling

def scale(image,scale_x,scale_y):
    scaled_image=np.zeros((int(image.shape[0]*scale_y),int(image.shape[1]*scale_x)))
    for i in range(scaled_image.shape[0]):
        for j in range(scaled_image.shape[1]):
            scaled_image[i][j]=image[int(i/scale_y)][int(j/scale_x)]
    return scaled_image

scaled_image=scale(image1,1.5,1.5)



