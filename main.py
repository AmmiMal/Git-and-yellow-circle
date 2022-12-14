import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randrange


class LoadUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')


class Example(LoadUI):
    def __init__(self):
        LoadUI.__init__(self)
        self.init()

    def init(self):
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        n = randrange(3, 50)
        for i in range(n):
            qp.setBrush(QColor(randrange(256), randrange(256), randrange(256)))
            diam = randrange(10, 50)
            qp.drawEllipse(randrange(400 - diam), randrange(400 - diam), diam, diam)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
