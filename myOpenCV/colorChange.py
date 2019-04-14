import cv2

# 打印图像色彩空间变换的类型
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(len(flags))
print(flags)

rgbImg1 = cv2.imread("imgs/t9.jpg")
cv2.imshow('Original', rgbImg1)
# cv2.cvtColor(rgbImg, cv2.COLOR_BGR2RGB)
grayImg = cv2.cvtColor(rgbImg1, cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY', grayImg)
if cv2.waitKey(0) == 27:
    cv2.destroyWindow('BGR2GRAY')
