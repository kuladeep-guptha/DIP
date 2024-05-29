#write python code for finding quality degraded image w.r.t original image using PSNR
#dont use inbuilt function for psnr
#to get degraded image you can blur the image or add guassian noise or compress using jpeg2000 and then decompress it
#you can use inbuitl function for these operations

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

img1 = cv2.imread('kula.jpg')
img2 = cv2.imread('kula.jpg')
img2 = cv2.blur(img2, (5,5))

#add gaussian noise
mean = 0
var = 0.1
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, img1.shape)
gaussian = gaussian.reshape(img1.shape[0], img1.shape[1], img1.shape[2]).astype('uint8')
img2 = cv2.add(img2, gaussian)




print(psnr(img1, img2))

plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()





#compress using JPEG 200 and then decompress it around 70% - 80%.
img1 = cv2.imread('kula.jpg')
cv2.imwrite('kula.jpg', img1, [int(cv2.IMWRITE_JPEG2000_COMPRESSION_X1000), 70])
img2 = cv2.imread('kula.jpg')
print(psnr(img1, img2))
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()





