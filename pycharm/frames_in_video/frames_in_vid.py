import cv2
print("package imported")
cap = cv2.VideoCapture("test1.mp4")
success, img = cap.read()
count =0
while success:
    #cv2.imwrite("frame%d.jpg" % count, img)
    success, img = cap.read()
    #print('Read a new frame: ', success)
    count +=1
print("Total number of frames in a video::",count)