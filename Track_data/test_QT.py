import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QWidget, QVBoxLayout
import Track_data.track_data_doc

class All_Track_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Все Авто")
        # self.resize(400, 800)
        widget_all = QWidget()
        mainLayout_all = QVBoxLayout()
        self.answer_all = QTextEdit('')
        mainLayout_all.addWidget(self.answer_all)
        widget_all.setLayout(mainLayout_all)
        self.setCentralWidget(widget_all)


def start_All_Track_Window():
    # app = QApplication(sys.argv)
    win = All_Track_Window()
    win.show()
    # sys.exit(app.exec_())

# if __name__ == '__main__':
start_All_Track_Window()
