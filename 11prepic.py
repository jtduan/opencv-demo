# -*- coding: utf-8 -*-
# 图像预处理：高通滤波器：去除噪音

import cv2
import numpy as np

img = cv2.imread('./resources/code13.png',cv2.IMREAD_GRAYSCALE)
dst=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Image", dst)
k = cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()
