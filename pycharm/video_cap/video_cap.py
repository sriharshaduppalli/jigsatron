import cv2
print("package imported")
cap = cv2.VideoCapture("C:/Users/sriha/Desktop/OpenCV/sample_videos/test1.mp4")

while True:
    success, img = cap.read()
    if not success:
        print("read not success")
        break
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break