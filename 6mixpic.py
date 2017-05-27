# -*- coding: utf-8 -*-

# 图片相加需要2个图片大小一致
import cv2
import numpy as np

img1 = cv2.imread('./resources/code13.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('./resources/code8.png', cv2.IMREAD_UNCHANGED)
height,width=img1.shape[:2]
img2 = cv2.resize(img2,(width,height),interpolation=cv2.INTER_CUBIC)
dst = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
