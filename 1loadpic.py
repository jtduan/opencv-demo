# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取图片以及加载的方式（灰度图，原图）
# cv2.IMREAD_COLOR (默认)
# cv2.IMREAD_GRAYSCALE （灰度图）
# cv2.IMREAD_UNCHANGED (原图)
img = cv2.imread("./resources/9.png", cv2.COLOR_BGR2GRAY)
# img= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=(0,0,255))

## 创建一个窗口，可以指定窗口的大小
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# 显示图片
cv2.imshow("Image", img)

# 等待键盘按下（参数为超时时间ms,超时返回-1）
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    # 写入图片，不会自动建立文件夹
    cv2.imwrite('./out/poli-gray.jpg', img)
cv2.destroyAllWindows()

# 将BGR转换为RGB后才能通过plt正确显示
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.imshow(img2)
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
