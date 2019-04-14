import cv2
import numpy as np

grayImg = cv2.imread("imgs/gray_img.png",0)
reverse_img = 255 - grayImg   # 对图像取反

random_img = np.zeros((grayImg.shape[0], grayImg.shape[1]), dtype=np.uint8)
# 对图像像素线性变换
for i in range(grayImg.shape[0]):
    for j in range(grayImg.shape[1]):
        random_img[i, j] = grayImg[i, j]*1.2
cv2.imshow('reverse_img', reverse_img)
cv2.imshow('random_img', random_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
