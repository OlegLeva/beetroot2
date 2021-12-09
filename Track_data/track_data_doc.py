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
        self.btn = QPushButton('Найти', self)
        self.head_Edit_Label = QLabel('Добавление информации')
        self.update_edit = QLineEdit('')
        self.update_edit.setPlaceholderText("Введите информацию")
        self.btn_2 = QPushButton('Добавить', self)
        self.answer = QTextEdit('')
        self.answer.setPlaceholderText("ANSWER")

        mainLayout = QVBoxLayout()
        findLoyaut = QHBoxLayout()
        editLoyaut = QHBoxLayout()

        findLoyaut.addWidget(self.request)
        findLoyaut.addWidget(self.btn)

        editLoyaut.addWidget(self.update_edit)
        editLoyaut.addWidget(self.btn_2)

        mainLayout.addWidget(self.head_Request_Label)
        mainLayout.addLayout(findLoyaut)
        mainLayout.addWidget(self.head_Edit_Label)
        mainLayout.addLayout(editLoyaut)
        mainLayout.addWidget(self.answer)

        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.car_json = [
            {
                'number': '9313',
                'data': ['BI9313EX', 'BI3866XF',
                         'Терещенко Дмитрий Анатольевич',
                         '+380980353438']
            },
            {
                'number': '8576',
                'data': ['BI8576EI', 'BI3844XF',
                         'Возный Андрей Юрьевич',
                         '+380679265219']
            }
        ]
        self.btn.clicked.connect(partial(self.get_find_text))
        self.btn_2.clicked.connect(partial(self.add_text))

    def get_find_text(self):
        for self.car_data in self.car_json:
            if self.car_data['number'] == self.request.text():
                text_print = ''
                for i in self.car_data['data']:
                    text_print += i+'\n'
                self.answer.setText(text_print)

    def add_text(self):
        print(self.car_json[0]['data'])
        for self.car_data in self.car_json:
            if self.car_data['number'] == self.request.text():
                self.car_data['data'].append(self.update_edit.text())




def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
