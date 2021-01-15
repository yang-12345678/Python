import qrcode
import cv2 as cv
import os
import sys
import time

QRImagePath = os.getcwd() + '/qrcode.png'  # 临时存储位置
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)  # 设置图片格式

data = cv.imread("C:\\Users\\Administrator\Desktop\\000.jpg")  # 运行时输入数据
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img.save('qrcode.png')  # 生成图片
