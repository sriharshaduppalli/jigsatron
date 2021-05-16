import cv2
import numpy as np

img = cv2.imread("C:/Users/sriha/Desktop/matlab_images/apj.jpg")
kernel = np.ones((5,5),np.uint8)

#convert RGB to GRAY
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#BLur image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#edge detector
imgCanny = cv2.Canny(img,150,200)

#image dialation thick edge
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

#image erode thin edge
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

#cv2.imshow("Gray Image",imgGray)
#cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)