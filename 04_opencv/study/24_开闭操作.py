# -*- coding=GBK -*-
import cv2 as cv


# ͼ��Ŀ��ղ���
def open_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("��ֵ��", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("������", binary)


def close_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("�ղ���", binary)


src = cv.imread("C://1.jpg")
cv.imshow("ԭ��", src)
open_image(src)
close_image(src)
cv.waitKey(0)
cv.destroyAllWindows()

'''ɾ��ͼ��С�ĸ�����'''
