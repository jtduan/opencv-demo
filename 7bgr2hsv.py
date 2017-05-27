# -*- coding: utf-8 -*-

# 图片相加需要2个图片大小一致
import cv2
import numpy as np

img1 = cv2.imread('./resources/Poli.jpg', cv2.IMREAD_UNCHANGED)
hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)