# -*- coding: utf-8 -*-

# 图片相加需要2个图片大小一致
import cv2
import numpy as np

img1 = cv2.imread('./resources/Poli.jpg', cv2.IMREAD_UNCHANGED)

rows, cols = img1.shape[:2]

# 平移
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img1,M,(cols,rows))

# 缩放
# res=cv2.resize(img1,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
dst = cv2.resize(img1, (600, 200), interpolation=cv2.INTER_CUBIC)

# 旋转:第一个参数为旋转中心 第二个为旋转角度 第三个为旋转后的缩放因子
# M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
# dst = cv2.warpAffine(img1, M, (cols, rows))

# 仿射变换
# pts1=np.float32([[50,50],[200,50],[50,200]])
# pts2=np.float32([[10,100],[200,50],[100,250]])
# M=cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(img1, M, (cols, rows))

while (1):
    cv2.imshow('img', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
