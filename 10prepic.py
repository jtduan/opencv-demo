# -*- coding: utf-8 -*-
# 图像预处理：图像平滑：低通滤波器：去除噪音

import cv2
import numpy as np

img1 = cv2.imread('./resources/code13.png')
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img1, -1, kernel)

cv2.namedWindow("Image")
cv2.imshow("Image", dst)
k = cv2.waitKey(0) & 0xFF

dst = cv2.blur(img1, (5, 5))
cv2.imshow("Image", dst)
k = cv2.waitKey(0) & 0xFF

dst = cv2.GaussianBlur(img1, (5, 5),0)
cv2.imshow("Image", dst)
k = cv2.waitKey(0) & 0xFF

dst = cv2.bilateralFilter(img1,9,75,75)
cv2.imshow("Image", dst)
k = cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()
