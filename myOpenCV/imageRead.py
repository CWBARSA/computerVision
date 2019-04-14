import cv2
gray_img = cv2.imread('imgs/t9.jpg', 0)  # 加载灰度图像
rgb_img = cv2.imread('imgs/t9.jpg', 1)    # 加载RGB彩色图像
cv2.imshow('Grey', gray_img)  # 显示灰度图像
cv2.imshow('RGB', rgb_img)  # 显示彩色图像
#if cv2.waitKey(0) == 27:  # 按空格退出窗口
    #cv2.destroyAllWindows()

cv2.imwrite('imgs/rgb_img1.jpg', rgb_img)    # 将图像保存成jpg文件
cv2.imwrite('imgs/gray_img1.png', gray_img)  # 将图像保存成png文件


# 当指定waitKey(0) == 27时当敲击键盘 Esc 时便销毁所有窗口
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

# 当接收到键盘敲击A时，便销毁名称为'RGB'的图像窗口
if cv2.waitKey(-1) == ord('A'):
    cv2.destroyWindow('RGB')

# 表示等待10秒，将销毁窗口名称为'Grey'的图像窗口
if cv2.waitKey(10000):
    cv2.destroyWindow('Grey')
# 表示等待10秒后，将销毁所有图像
if cv2.waitKey(10000):
    cv2.destroyAllWindows()

