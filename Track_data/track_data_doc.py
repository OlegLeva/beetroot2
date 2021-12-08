from functools import partial
import psycopg2
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QGridLayout,
                             QPushButton,
                             QSizePolicy,
                             QTextEdit)

import sys


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Данные автомобиля")
        self.setGeometry(300, 100, 800, 500)
        widget = QWidget()
        self.head_Request_Label = QLabel('Выбор авто')
        self.request = QLineEdit('')
        self.request.setPlaceholderText("Введите номер авто")
        self.btn = QPushButton('Найти')
        self.head_Edit_Label = QLabel('Добавление информации')
        self.update_edit = QLineEdit('')
        self.update_edit.setPlaceholderText("Введите информацию")
        btn_2 = QPushButton('Добавить')
        self.answer = QTextEdit('')
        self.answer.setPlaceholderText("ANSWER")

        mainLayout = QVBoxLayout()
        findLoyaut = QHBoxLayout()
        editLoyaut = QHBoxLayout()

        findLoyaut.addWidget(self.request)
        findLoyaut.addWidget(self.btn)

        editLoyaut.addWidget(self.update_edit)
        editLoyaut.addWidget(btn_2)

        mainLayout.addWidget(self.head_Request_Label)
        mainLayout.addLayout(findLoyaut)
        mainLayout.addWidget(self.head_Edit_Label)
        mainLayout.addLayout(editLoyaut)
        mainLayout.addWidget(self.answer)

        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    car_json = [
        {
            'number': 'BI9313EX',
            'data': ['BI9313EX', 'BI3866XF',
                     'Терещенко Дмитрий Анатольевич',
                     '+380980353438']
        },
        {
            'number': 'BI8576EI',
            'data': ['BI8576EI', 'BI3844XF',
                     'Терещенко Дмитрий Анатольевич',
                     '+380980353438']
        }
    ]

    def get_find_text(self, text=''):
        self.request.setText(self.request.text() + text)

def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
