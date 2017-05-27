# -*- coding: utf-8 -*-
# Todo: 保存视频无法打开
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取视频（参数为文件名）或者摄像头（参数为设备号）
cap = cv2.VideoCapture(0)

# 跳转摄像头配置，3和4代表宽和高
cap.set(3, 320)
cap.set(4, 240)  # Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('./out/output.avi', fourcc, 10, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
