# -*- coding=GBK -*-
import cv2 as cv


# �������
def face_image():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("../project/cascades/haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray, 1.02, 1)  # �ڶ����������ƶ����룬������������ʶ��ȣ�Խ��ʶ���Խ��
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)  # ������������һ������ɫ��һ���Ǳ߿���
    cv.imshow("output", src)


src = cv.imread("face.jfif")
cv.imshow("input", src)
face_image()
cv.waitKey(0)
cv.destroyAllWindows()

# -*- coding=GBK -*-
# import cv2 as cv
#
#
# # ����ͷ�������
# def face_image(src):
#     gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
#     face_detector = cv.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
#     faces = face_detector.detectMultiScale(gray, 1.02, 5)  # �ڶ����������ƶ����룬������������ʶ��ȣ�Խ��ʶ���Խ��
#     for x, y, w, h in faces:
#         cv.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)  # ������������һ������ɫ��һ���Ǳ߿���
#     cv.imshow("���", src)
#
#
# capture = cv.VideoCapture(0)
# while True:
#     ret, frame = capture.read()
#     frame = cv.flip(frame, 1)
#     face_image(frame)
#     if cv.waitKey(10) & 0xFF == ord('q'):  # ��������q�˳����ڣ�����q����رջ�һֱ�ز��� Ҳ�������ó���������
#         break
# face_image()
# cv.waitKey(0)
# cv.destroyAllWindows()