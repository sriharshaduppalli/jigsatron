import cv2
print("package imported")
cap = cv2.VideoCapture("test1.mp4")

# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver) < 3:
  fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
  print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else:
  fps = cap.get(cv2.CAP_PROP_FPS)
  print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

success, img = cap.read()
count =0
while success:
    #cv2.imwrite("frame%d.jpg" % count, img)
    success, img = cap.read()
    #print('Read a new frame: ', success)
    count +=1
print("Total number of frames in a video::",count)