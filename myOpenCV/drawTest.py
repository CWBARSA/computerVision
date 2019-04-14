import cv2
import numpy as np

img0 = np.ones((512,512,3), np.uint8)
img = 255*img0
img = cv2.line(img, (100,100), (400,400),(255, 0, 0), 5)
img = cv2.rectangle(img,(200, 20),(400,120),(0,255,0),3)
img = cv2.circle(img,(100,400), 50, (0,0,255), 2)
img = cv2.circle(img,(250,400), 50, (0,0,255), 0)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,(0, 255, 255), -1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
img = cv2.polylines(img,[pts],True,(0, 0, 0), 2)

cv2.imshow('img', img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
