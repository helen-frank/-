import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


if __name__ == '__main__':

    app = QApplication([])
    window = QMainWindow()
    window.resize(400, 500)
    window.move(600, 200)
    window.setWindowTitle("脸型发型匹配数据生成")

    str1 = sys.argv[1]
    str1 = str1.replace("#", " ")
    str1 = str1.replace("@","\n")
    str2 = sys.argv[2]
    str2 = str2.replace("#", " ")
    str2 = str2.replace("@","\n")
    str3 = sys.argv[3]
    str3 = str3.replace("#", " ")
    str3 = str3.replace("@", "\n")

    textEdit_1 = QTextEdit(window)
    #textEdit_1.setObjectName("textEdit")
    textEdit_1.setReadOnly(True)
    textEdit_1.move(10, 60)
    textEdit_1.resize(380, 420)

    textEdit_1.append(str1)
    textEdit_1.append(str2)
    textEdit_1.append(str3)

    window.show()
    app.exec_()
