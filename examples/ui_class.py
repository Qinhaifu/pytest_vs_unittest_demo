import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def show_ui(data):
    app = QApplication(sys.argv)
    win = UITestDemo()  # class instance
    win.show(data)
    # sys.exit(app.exec_())
    if data != 1000:
        return False
    return True


class UITestDemo(QWidget):
    def __init__(self, parent=None):
        super(UITestDemo, self).__init__(parent)
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle("UITestDemo")  # set window title
        quit = QPushButton("Close", self)  # button
        quit.setGeometry(10, 10, 100, 60)  # button postion and size
        quit.setStyleSheet("background-color: red")  # button style and color
        quit.clicked.connect(self.close)  # button callback

        self.timer = QTimer(self)  # init a timer
        self.timer.timeout.connect(self.close)  # callback
        self.timer.start(2000)  # 2000ms

    def show(self, data):
        super(UITestDemo, self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UITestDemo()  # class instance
    win.show()
    sys.exit(app.exec_())
