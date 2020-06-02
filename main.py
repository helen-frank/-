import requests
import simplejson
import json
import base64
from aip import AipFace
import sys
import os
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

str1 = "欢迎使用本系统\n\n本系统可实现识别人脸脸型，颜值，年龄等数据，并为对应的脸型提供合适的发型\n\n为你和模特进行换脸，展现颜值巅峰（可能是）\n\n使用方法:\n在上述文本框中输入你的图片地址绝对路径，相对路径（放置于当前目录下）皆可，点击确定开始运行"
str2 = ""
str3 = ""
def shibe(file):
    """ 你的 APPID AK SK """
    APP_ID = '17817245'
    API_KEY = 'k1KhcY1c1v8MtiwF45XmkM5t'
    SECRET_KEY = 'G7QxCRnjz1Yep3Grjn1vD6xWNp4vLdqX'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    with open(file, "rb") as f:
        data = f.read()
        encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
        images = str(encodestr, 'utf-8')  # 重新编码数据
    image = images
    imageType = "BASE64"

    """ 脸型推荐 """
    face_recommend_man = {'正方形': '男:\n    特点：额骨较宽，脸部下三分之一宽而阔，脸部线条刚硬，给人一种严肃感。\n    在历来审美观念更替中，这依然是最有男人味的一种脸型。\n    适合发型：卡尺头发型、露额短发、大背头发型、纹理烫发型等等。',
                          '三角形': '男：\n    三角形脸也叫梨形脸，主要特点是额头窄，脸部有肉感或者下颌骨较宽。\n    因为额头较窄、脸部较大，不管是脸肥型还是下颌骨宽大型，在挑选发型时都需要注意不要将额头两侧的头发理净，最好留一部分与脸部同宽，或将头顶的头发做蓬松，增加头上部的宽度或遮盖住小额头。\n    适合的发型：后梳头、碎发、层次飞机头、自然刘海',
                          '椭圆': '男：\n    特点：脸部纵向长度长，脸型大，给人感觉显老气。\n    适合发型：刘海型发型减少脸部长度，不可露出发际线！\n    如果实在不喜欢有刘海，梳油头也可，不过对颜值要求更高，慎重啊！更是忌寸头！',
                          '心形': '男：\n    特点：心形脸是众多脸型中比较完美的脸型,上宽下窄。\n    适合发型：四六分刘海发型、飞机头、蓬松刘海发型、fzl斜刘海等等。\n    心形脸的男生是对发型最不挑剔的，可谓是百搭款，剪任何发型对脸型的影响都不大，尽管是寸头都无所畏惧。\n    ',
                          '圆形': '男：\n    特点：腮和下巴的弧度比较圆，分界不明显；脸部的长宽近似。\n    适合发型：四六分心形刘海发型，短卷发齐刘海，齐刘海短发等发型。（刘海是个好东西....）'}

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,expression,face_shape,gender,glasses,emotion,face_probability,eye_status,landmark,quality"

    """ 带参数调用人脸检测 """
    m = client.detect(image, imageType, options)
    if m["error_msg"] == "SUCCESS":
        mm = m["result"]
        """"print(mm)"""
        num = mm["face_num"]
        mmm = mm["face_list"][0]
        age = mmm["age"]
        beauty = mmm["beauty"]

        # 表情
        exp = {'none': "不笑", 'smile': "微笑", 'laugh': "大笑"}
        expression = mmm["expression"]['type']
        if expression in exp:
            expressions = exp[expression]
        else:
            expressions = "未知"

        # 脸型
        face = {'square': '正方形', 'triangle': '三角形',
                'oval': '椭圆', 'heart': '心形', 'round': '圆形'}
        face_shape = mmm["face_shape"]['type']
        if face_shape in face:
            face_shapes = face[face_shape]
        else:
            face_shapes = "未知"

        # 性别
        gen = {'male': '男', 'female': '女'}
        gender = mmm["gender"]['type']
        if gender in gen:
            genders = gen[gender]
        else:
            genders = "未知"

        # 眼镜
        gla = {'none': '无眼镜', 'common': '普通眼镜', 'sun': '墨镜'}
        glasses = mmm["glasses"]['type']
        if glasses in gla:
            glassess = gla[glasses]
        else:
            glassess = "未知"

        # 情绪
        emo = {'angry': '愤怒', 'disgust': '厌恶', 'fear': '恐惧',
               'happy': '高兴', 'sad': '伤心', 'surprise': '惊讶', 'neutral': '无情绪'}
        emotion = mmm["emotion"]['type']
        if emotion in emo:
            emotions = emo[emotion]
        else:
            emotions = "未知"

        global str1
        global str2

        print("人脸数：%d, 年龄：%d, 性别： %s, 颜值：%d, 表情：%s, 脸型：%s, 眼镜：%s, 情绪：%s"
              % (num, age, genders, beauty, expressions, face_shapes, glassess, emotions))
        str1 = "图片检测数据\n人脸数："+str(num)+", 年龄："+str(age)+", 性别："+genders+", 颜值："+str(beauty)+", 表情："+expressions+", 脸型："+face_shapes+", 眼镜："+glassess+", 情绪："+emotions+"\n\n"
        str1 = str1.replace(" ", "#")
        str1 = str1.replace("\n","@")
        if genders == '男':
            for face_shapes_t in face_recommend_man:
                if face_shapes_t == face_shapes:
                    print(face_shapes_t + ':' +
                          face_recommend_man[face_shapes_t])
                    str2 = face_shapes_t + ':' + face_recommend_man[face_shapes_t]
                    str2 = str2.replace(" ", "#")
                    str2 = str2.replace("\n","@")
                    break
        else:
            print('女性正在正在开发中')
            str2 = "女性正在开发中"
    else:
        print("人脸有误，请保证光照的情况,以及正面拍照")
        str2 = "人脸有误，请保证光照的情况,以及正面拍照"
    return face_shapes


def shibe_o(file):
    """ 你的 APPID AK SK """
    APP_ID = '17817245'
    API_KEY = 'k1KhcY1c1v8MtiwF45XmkM5t'
    SECRET_KEY = 'G7QxCRnjz1Yep3Grjn1vD6xWNp4vLdqX'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    with open(file, "rb") as f:
        data = f.read()
        encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
        images = str(encodestr, 'utf-8')  # 重新编码数据
    image = images
    imageType = "BASE64"

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,expression,face_shape,gender,glasses,emotion,face_probability,eye_status,landmark,quality"

    """ 带参数调用人脸检测 """
    m = client.detect(image, imageType, options)
    if m["error_msg"] == "SUCCESS":
        mm = m["result"]
        """print(mm)"""
        num = mm["face_num"]
        mmm = mm["face_list"][0]
        age = mmm["age"]
        beauty = mmm["beauty"]

    # 表情
        exp = {'none': "不笑", 'smile': "微笑", 'laugh': "大笑"}
        expression = mmm["expression"]['type']
        if expression in exp:
            expressions = exp[expression]
        else:
            expressions = "未知"

        global str3

        print("年龄：%d, 颜值：%d, 表情：%s"
              % (age, beauty, expressions))
        str3 = "\n\n更换发型后可能的数据\n年龄："+str(age)+", 颜值："+str(beauty)+", 表情："+expressions
        str3 = str3.replace(" ", "#")
        str3 = str3.replace("\n","@")
    else:
        print("人脸有误")
        str3 = "人脸有误"

def find_face(imgpath):

    print("开始替换生成图片ing")
    # 调用相应的api
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    # 获取自己的账号
    data = {"api_key": 'FQR0wMTpCAqSzezYNxX0xWJ2QzmQyfGx',
            "api_secret": 'WZZiVbe4lUY6kyU5SCVeT3mKf-iy9uii', "image_url": imgpath, "return_landmark": 1}

    files = {"image_file": open(imgpath, "rb")}

    response = requests.post(http_url, data=data, files=files)

    req_con = response.content.decode('utf-8')

    req_dict = json.JSONDecoder().decode(req_con)

    this_json = simplejson.dumps(req_dict)

    this_json2 = simplejson.loads(this_json)

    faces = this_json2['faces']

    list0 = faces[0]

    rectangle = list0['face_rectangle']

    print(rectangle)

    return rectangle


def merge_face(image_url_1, image_url_2, image_url, number):

    ff1 = find_face(image_url_1)

    ff2 = find_face(image_url_2)

    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) +
                     "," + str(ff1['width']) + "," + str(ff1['height']))

    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + \
        "," + str(ff2['width']) + "," + str(ff2['height'])

    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"

    f1 = open(image_url_1, 'rb')

    f1_64 = base64.b64encode(f1.read())

    f1.close()

    f2 = open(image_url_2, 'rb')

    f2_64 = base64.b64encode(f2.read())

    f2.close()

    data = {"api_key": 'rnoaJExcaeDt5H3_QgTfS61ZWEsWRW1B', "api_secret": 'Vkv5lSzXgM5syr0guXuDYTshzQQRSM9f',
            "template_base64": f1_64, "template_rectangle": rectangle1,
            "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}

    response = requests.post(url_add, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = json.JSONDecoder().decode(req_con)

    result = req_dict['result']

    imgdata = base64.b64decode(result)

    file = open(image_url, 'wb')

    file.write(imgdata)

    file.close()


def test(load,face):
    image1 = load
    if face == "正方形":
        image2 = "./脸型/正方形.jpg"
        image = "./output.jpg"
    elif face == "三角形":
        image2 = "./脸型/三角形.jpg"
        image = "./output.jpg"
    elif face == "椭圆":
        image2 = "./脸型/椭圆.png"
        image = "./output.jpg"
    elif face == "心形":
        image2 = "./脸型/心形脸.png"
        image = "./output.jpg"
    elif face == "圆形":
        image2 = "./脸型/圆脸.png"
        image = "./output.jpg"

    merge_face(image2, image1, image, 50)

def handlecalc():  #点击事件
    q=textEdit.toPlainText()
    if (':' in q):
        load = q
    else:
        load = "./图片/"+q
    face = shibe(load)
    test(load, face)
    shibe_o("./output.jpg")
    os.system("start python -u text.py %s %s %s" % (str1, str2, str3))

    #os.system("start python -u text.py")
    os.system("python -u output.py")

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    window.resize(400, 500)
    window.move(200, 200)
    window.setWindowTitle("脸型发型匹配")

    textEdit = QTextEdit(window)
    textEdit.setPlaceholderText("请输入文件地址")
    textEdit.move(10, 25)
    textEdit.resize(290, 30)


    textEdit_1 = QTextEdit(window)
    #textEdit_1.setObjectName("textEdit")
    textEdit_1.setReadOnly(True)
    textEdit_1.setPlaceholderText("等待进程ing")
    textEdit_1.move(10, 60)
    textEdit_1.resize(380, 420)

    button = QPushButton('确定', window)
    button.move(300, 25)
    button.clicked.connect(handlecalc)

    textEdit_1.append(str1)

    window.show()
    app.exec_()
