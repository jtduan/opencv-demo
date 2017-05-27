# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 当 标按下时变为 True
drawing = False
# 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix, iy = -1, -1


# 创建回 函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 3)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

events=[i for i in dir(cv2) if 'EVENT'in i]
print events