# 调用百度API完成人脸识别
"""
Created on 2020-09-05
@author: gouyu
"""

import requests
import base64
import tkinter.filedialog
from .dictionary import recommend
import cv2

def get_access_token(client_id, client_secret):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # 帮助文档
    # https://ai.baidu.com/docs#/Auth/top
    # 帮助文档中python代码基于python2,本文已经转换为python3x调试通过。
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    header = {'Content-Type': 'application/json; charset=UTF-8'}
    response1 = requests.post(url=host, headers=header)  # <class 'requests.models.Response'>
    json1 = response1.json()  # <class 'dict'>
    access_token = json1['access_token']

    return access_token


def open_pic2base64():
    # 本地图片地址，根据自己的图片进行修改
    # 打开本地图片，并转化为base64
    root = tkinter.Tk()  # 创建一个Tkinter.Tk()实例
    root.withdraw()  # 将Tkinter.Tk()实例隐藏
    # file_path = tkinter.filedialog.askopenfilename(title=u'选择文件')
    file_path = 'F:/1scshixi/OpenCV-Emotion-Recognition-master/OpenCV-Emotion-Recognition-master/take_pic/tp1.jpg'
    f = open(file_path, 'rb')
    img = base64.b64encode(f.read()).decode('utf-8')
    return img


def bd_rec_face(client_id, client_secret):
    # 识别人脸，给出性别、年龄、人种、颜值分数、是否带眼镜等信息
    # 帮助文档中python代码基于python2,本文已经转换为python3x调试通过。

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = {"image": open_pic2base64(), "image_type": "BASE64",
              "face_field": "age,beauty,glasses,gender,race,emotion"}
    header = {'Content-Type': 'application/json'}

    access_token = get_access_token(client_id, client_secret)  # '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token

    request_url = request_url + "?access_token=" + access_token
    response1 = requests.post(url=request_url, data=params, headers=header)
    json1 = response1.json()
    print("性别为", json1["result"]["face_list"][0]['gender']['type'])
    print("年龄为", json1["result"]["face_list"][0]['age'], '岁')
    print("人种为", json1["result"]["face_list"][0]['race']['type'])
    print("颜值评分为", json1["result"]["face_list"][0]['beauty'], '分/100分')
    print("是否带眼镜", json1["result"]["face_list"][0]['glasses']['type'])
    print("情绪", json1["result"]["face_list"][0]['emotion']['type'])
    print(str(json1["result"]["face_list"][0]['emotion']['type']))
# 情绪：angry 厌恶：disgust 恐惧：fear 高兴：happy 伤心：sad 惊讶：surprise 无情绪：neutral
    if str(json1["result"]["face_list"][0]['emotion']['type'])=='sad':
        recommend('1')

def face_rec_start():
    # 以下为代码功能测试：
    # 账户id，client_id 为官网获取的AK， client_secret 为官网获取的SK。
    # https://console.bce.baidu.com/ai/?fromai=1#/ai/face/app/list
    client_id = 'gcSD08QbkwkILlDBAamRlpXl'  # ak
    client_secret = 'GfSEI9Va3OrSKhzzC5chp2GbD0woCRwb'  # sk

    # 实例1：人脸识别
    bd_rec_face(client_id, client_secret)