#color detection
import cv2
import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture(0) # 0 for default webcam, 1 for other
cap.set(3, 640)  # id for width= 3
cap.set(4, 480)  # id for height= 4
cap.set(10, 100)  #id for brightness= 10
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# path = 'Resources/avi.jpg'
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640,240)
cv2.createTrackbar("Hue Min", "Trackbars", 0,179, empty)  #name, window name, min value, max value, function
cv2.createTrackbar("Hue Max", "Trackbars", 179,179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0,255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255,255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0,255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255,255, empty)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    #set values using mask to h_min , h_max and so on to get the mask
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    # cv2.imshow("Resize", imgResize)
    # cv2.waitKey(1)