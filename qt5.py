import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Третье окно')
        helloWorldLabel = QLabel('<b><i>Hello</b></i>')
        self.setCentralWidget(helloWorldLabel)

def main_widget():
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Моё второе окно')
    # mainWidget.setFixedSize(500, 500)
    mainWidget.setGeometry(50, 70, 500, 500)
    helloWorldLabel = QLabel('<b><i>Hello</b></i>', parent=mainWidget)
    helloWorldLabel.move(10, 25)
    mainWidget.show()
    app.exec()

def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
