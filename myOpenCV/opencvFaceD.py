#  OpenCV 7行代码检测人脸

import cv2

face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

sample_image = cv2.imread('imgs/t9.jpg')

faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100))

for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('imgs/20190414_largestSelfie.jpg', sample_image);

cv2.imshow('faceD',sample_image)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindow()