import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLineEdit,
                             QMainWindow,
                             QHBoxLayout,
                             QPushButton,
                             QVBoxLayout,
                             QGridLayout,
                             QLabel)

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Третье окно')
        self.setGeometry(50, 70, 500, 500)
        widget = QWidget()
        kukuLabel = QLabel('<h1>Kuku</h1>')
        editArea = QLineEdit('0')
        mainButtom = QPushButton('Push')
        mainButtom_2 = QPushButton('Second Push')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(kukuLabel)
        mainLayout.addWidget(editArea)

        mainLayout.addWidget(mainButtom)
        mainLayout.addWidget(mainButtom_2)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

#
# def main_widget():
#     app = QApplication(sys.argv)
#     mainWidget = QWidget()
#     mainWidget.setWindowTitle('Моё второе окно')
#     # mainWidget.setFixedSize(500, 500)
#     mainWidget.setGeometry(50, 70, 500, 500)
#     helloWorldLabel = QLabel('<b><i>Hello</b></i>', parent=mainWidget)
#     helloWorldLabel.move(10, 25)
#     mainWidget.show()
#     app.exec()

def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
