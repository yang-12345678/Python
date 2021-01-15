import os
import time
import json
import pyttsx3
import threading
import cv2 as cv
import numpy as np
from datetime import datetime
from pyttsx3.voice import Voice

count = 0
label = 0


# 采集人脸信息
def face_collect():
    # 获取XML文件，加载人脸检测器
    dic = {}  # 存放成员信息
    face_cascade = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
    video = cv.VideoCapture(0)
    name = input("请输入采集人的信息(格式：编号_姓名)：")
    str_num = name.split("_")  # 存放成员的序号
    dic.setdefault("{}".format(str_num[0]), "{}".format(str_num[1]))
    ret = json.dumps(dic)
    os.mkdir("./data/{}".format(str_num[0]))
    with open("./database/{}.txt".format(str_num[0]), "a", encoding="utf-8") as f:
        f.write(ret)

    while True:
        # 读取当前帧
        ret, frame = video.read()
        # 调转摄像头
        frame = cv.flip(frame, 1)

        # 转换为灰度图像
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # 调用方法detectMultiScale检测人脸
        # 待检测图像（通常为灰度），前后两次扫描中窗口缩放比例，
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=6,
            minSize=(5, 5)
        )

        # 画矩形 在frame图片上画， 传入左上角和右下角坐标 矩形颜色 和线条宽度
        for (x, y, w, h) in faces:
            global count
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            f = cv.resize(gray[y:y + h, x:x + w], (200, 200))
            cv.imwrite("./data/{}/{}.pgm".format(str_num[0], str(count)), f)
            count += 1

        cv.imshow("dec_face", frame)
        if cv.waitKey(50) == 27:
            break
    video.release()
    cv.destroyAllWindows()


# 读取图片
def read_images():
    x, y = [], []
    path = "./data/"
    # 列出data文件夹下的所有内容  yang....
    image_file = os.listdir(path)
    # print(type(image_file))    列表类型

    # 得到所有形如./data/yang/  ...  路径  zhao qian sun li
    image_files = [path + i for i in image_file]
    for file in image_files:
        # ./data/yang路径下所有内容，即为图片
        images = os.listdir(file)

        label_name = file.split("/")[-1]
        for i in images:
            # ./data/yang/{}.pgm
            img = cv.imread(file + "/" + i, cv.IMREAD_GRAYSCALE)
            img = cv.resize(img, (200, 200))
            # x列表中存每个图片的信息
            # y列表中存每个图片对应的标签
            x.append(np.asarray(img, dtype=np.uint8))
            y.append(int(label_name))

    y = np.asarray(y, dtype=np.int32)
    return x, y


def sound(sentence):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    # 控制语音播放的速度
    engine.setProperty('rate', 130)
    volume = engine.getProperty('volume')
    # 控制语音播放的音量大小
    engine.setProperty('volume', 1.0)
    # voice = engine.getProperty('voice')
    # print(voice)

    v = Voice(id=1, name='lulu', languages='chinese', age=10, gender='男')
    engine.setProperty('voice', v)
    engine.say(sentence)
    engine.runAndWait()  # 朗读一次


def face_rec():
    # 获取数据
    x, y = read_images()

    model = cv.face.LBPHFaceRecognizer_create()
    """
    LBPH 产生评分不同，低于60是可靠的 高于80是不可靠的
    """

    # 训练模型
    model.train(np.asarray(x), np.asarray(y))

    # 开摄像头
    camera = cv.VideoCapture(0)
    # 加载检测人脸对象
    face_cascade = cv.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
    while True:
        # 读取当前帧
        ret, frame = camera.read()
        frame = cv.flip(frame, 1)
        # 当前帧下检测人脸
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=6,
            minSize=(5, 5)
        )
        for (x, y, w, h) in faces:
            # 画出人脸
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi = gray[x: x + w, y: y + h]
            try:
                # 更改大小
                roi = cv.resize(roi, (200, 200))
                # 进行预测
                params = model.predict(roi)
                # params是一个二元素列表, 第一个元素是预测结果，第二个元素是得分情况
                # 在图像上写预测结果  添加的文字， 左上角坐标
                # 1.2是字体大小 2是粗细
                global count
                global label
                if params[1] < 70:
                    label = params[0]
                    frame = cv.putText(frame, str(params[:]), (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                    count += 1

                # print(params)
            except Exception:
                pass
        cv.imshow("detect face", frame)
        if cv.waitKey(50) == 27:
            break


cv.destroyAllWindows()


def task1():
    face_rec()


def task2():
    with open('./database/{}.txt'.format(str(label)), 'r') as f:
        dic_name = json.load(f)
    t = datetime.now()

    while True:
        if count > 20:
            with open("./record/record.txt", "a", encoding='utf-8') as f:
                f.write("\n\n姓名:" + dic_name.get("{}".format(label)) + "\n打卡时间:" + t.strftime("%Y-%m-%d %H:%M:%S"))
                sound("签到成功")
                exit()
        else:
            pass


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)


def main():
    t1.start()
    time.sleep(10)
    t2.start()


# face_collect()

main()
