import cv2
import numpy as np

img = cv2.imread("C:/Users/sriha/Desktop/matlab_images/apj1.jpg")
#find size image
print(img.shape)

#resize image
imgResize = cv2.resize(img,(400,200))
print(imgResize.shape)

#image crop
imgCropped = img[0:200,200:500]

cv2.imshow("APJ",img)
#cv2.imshow("APJ resize",imgResize)
cv2.imshow("APJ cropped",imgCropped)
cv2.waitKey(0)