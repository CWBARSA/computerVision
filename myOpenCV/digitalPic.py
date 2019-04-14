import cv2
# 这里图像采用的仍旧是上面用的图像
rgb_img = cv2.imread('imgs/t9.jpg')
print(rgb_img.shape)     #(384, 512, 3)
print(rgb_img[0, 0])     #[71 50 23]
print(rgb_img[0, 0, 0])  #71

gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)    #(384, 512)
print(gray_img[0, 0])    #44
