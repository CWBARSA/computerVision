import cv2
import numpy as np

white_img = np.ones((512, 512, 3), np.uint8)
print(type(white_img))
black_img1 = 0 * white_img   # 纯黑色图像
white_img1 = 255 * white_img  # 纯白色图像
cv2.imshow('white_img', white_img1)
cv2.imshow('black_img', black_img1)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
