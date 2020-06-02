import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example (QWidget):
    def __init__(self):
        super ().__init__()
        self.initUI ()

    def initUI(self):
        hbox = QHBoxLayout (self)
        lbl = QLabel(self)
        pixmap = QPixmap("./output.jpg")  # 按指定路径找到图片
        lbl.setPixmap (pixmap)  # 在label上显示图片
        lbl.setScaledContents (True)  # 让图片自适应label大小
        #lbl.setPixmap(QPixmap(""))#移除label上的图片
        hbox.addWidget(lbl)

        self.setLayout (hbox)
        self.move (1200, 200)
        self.setWindowTitle ('明星换脸图，可能是该脸型的颜值倾向')
        self.show ()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example ()
    sys.exit (app.exec_())
