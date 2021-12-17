from functools import partial
import json
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QPushButton,
                             QTextEdit)

import sys


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Данные автомобиля")
        self.setGeometry(300, 100, 800, 500)
        widget = QWidget()

        custom_font = QFont()
        custom_font.setWeight(18)
        QApplication.setFont(custom_font, "QLabel")

        self.head_Request_Label = QLabel('Выбор авто')
        self.request = QLineEdit('')
        self.request.setPlaceholderText("Введите номер авто")
        self.btn = QPushButton('Найти', self)
        self.btn.setStyleSheet('background: rgb(197, 237, 237);')
        self.btn.setFixedSize(150, 30)
        self.add_track = QLineEdit('')
        self.add_track.setPlaceholderText("Введите данные нового авто")
        self.btn_add = QPushButton('Добавить', self)
        self.btn_add.setFixedSize(150, 30)
        self.btn_add.setStyleSheet('background: rgb(223, 235, 233);')
        self.btn_save = QPushButton('Сохранить', self)
        self.btn_save.setFixedSize(150, 30)
        self.btn_save.setStyleSheet('background: rgb(235, 223, 224);')
        self.btn_del = QPushButton('Удалить', self)
        self.btn_del.setFixedSize(150, 30)
        self.btn_del.setStyleSheet('background: rgb(250, 190, 190);')
        self.btn_edit = QPushButton('Сохранить изменения', self)
        self.btn_edit.setFixedSize(150, 30)
        self.btn_edit.setStyleSheet('background: rgb(250, 190, 190);')
        self.head_Edit_Label = QLabel('Добавление информации')
        self.update_edit = QLineEdit('')
        self.request.setStyleSheet("color: gray;"
                                       "background: rgb(217, 250, 244);"
                                       "selection-color: green;"
                                       "selection-background-color: blue;")
        self.add_track.setStyleSheet("color: gray;"
                                       "background: rgb(217, 250, 244);"
                                       "selection-color: green;"
                                       "selection-background-color: blue;")
        # self.update_edit.setFixedSize(600, 30)
        self.request.setFixedSize(600, 30)
        self.add_track.setFixedSize(750, 30)
        # self.update_edit.setPlaceholderText("Введите информацию")
        self.btn_2 = QPushButton('ДАННЫЕ ВСЕХ АВТО', self)
        self.btn_2.setFixedSize(250, 30)
        # self.btn_2.setStyleSheet('background: rgb(197, 237, 238);')

        self.answer = QTextEdit('')
        self.answer.setPlaceholderText("")

        mainLayout = QVBoxLayout()
        add_carLayout = QVBoxLayout()
        findLoyaut = QHBoxLayout()
        editLoyaut = QHBoxLayout()

        add_carLayout.addWidget(self.add_track)
        add_carLayout.addWidget(self.btn_add)
        add_carLayout.addWidget(self.btn_save)
        add_carLayout.addWidget(self.btn_del)

        findLoyaut.addWidget(self.request)
        findLoyaut.addWidget(self.btn)

        # editLoyaut.addWidget(self.update_edit)
        editLoyaut.addWidget(self.btn_2)

        mainLayout.addLayout(add_carLayout)
        mainLayout.addWidget(self.head_Request_Label)
        mainLayout.addLayout(findLoyaut)
        # mainLayout.addWidget(self.head_Edit_Label)
        mainLayout.addLayout(editLoyaut)
        mainLayout.addWidget(self.answer)
        mainLayout.addWidget(self.btn_edit)

        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        f = open("data.json")

        try:
            self.car_json = json.load(f)
        except json.decoder.JSONDecodeError:
            self.car_json = []
        f.close()

        self.patern_dict = {
            'number': '',
            'data': []
        }

        self.dump_json()
        self.btn.clicked.connect(partial(self.get_find_text))
        # self.btn.clicked.connect(EnterToken(self))
        self.btn_add.clicked.connect(partial(self.add_auto))
        self.btn_add.clicked.connect(self.add_track.clear)
        self.btn_save.clicked.connect(partial(self.save_auto))
        self.btn_save.clicked.connect(self.add_track.clear)
        self.btn_del.clicked.connect(partial(self.del_auto))
        self.btn_del.clicked.connect(self.add_track.clear)
        self.btn_edit.clicked.connect(partial(self.edit_data_auto))
        self.btn_2.clicked.connect(partial(self.get_all))

    def get_all(self):
        all_text = ''
        for self.car_data in self.car_json:
            text_print = f'<h3>{self.car_data["number"]} </h3>'
            self.car_data['data'].append("___________________________")
            for i in self.car_data['data']:
                text_print += f"<h3>{i}\n<\h3>"
            all_text += text_print
            self.answer.setText(all_text)


    def edit_data_auto(self):
        new_list = [i.strip() for i in self.answer.toPlainText().split('\n')]
        number = new_list.pop(0)
        for self.car_data in self.car_json:
            if number == self.car_data['number']:
                self.car_json.remove(self.car_data)
                print(number)
                self.patern_dict['number'] = number
                self.patern_dict['data'] = new_list
                new_dict = self.patern_dict
                self.patern_dict = {
                    'number': '',
                    'data': []
                }
                self.car_json.append(new_dict)

            self.dump_json()

    def del_auto(self):
        for self.car_data in self.car_json:
            if not self.add_track.text():
                self.answer.setText('<h2>Введите номер авто или часть номера</h2>')
            elif self.add_track.text() in self.car_data['number']:
                self.car_json.remove(self.car_data)
                self.dump_json()
                text_print = f'<h3>Автомобиль {self.car_data["number"]} удалён</h3>'
                self.answer.setText(text_print)
            else:
                self.answer.setText('<h2>Нет такого автомобиля</h2>')

    def add_auto(self):
        for self.car_data in self.car_json:
            if self.add_track.text() == self.car_data['number']:
                self.answer.setText(f"<h3>Автомобиль {self.add_track.text()} уже существует!!!<\h3>")
                return
        if self.patern_dict['number'] == '':
            self.patern_dict['number'] = self.add_track.text()
        elif self.patern_dict['number']:
            self.patern_dict['data'].append(self.add_track.text())
        text_print = f'<h3>{self.patern_dict["number"]}</h3>'
        if self.patern_dict['data']:
            for i in self.patern_dict['data']:
                text_print += f"<h3>{i}\n<\h3>"
        self.answer.setText(text_print)

    def save_auto(self):
        new_dict = self.patern_dict.copy()
        self.car_json.append(new_dict)
        self.patern_dict = {
            'number': '',
            'data': []
        }
        self.dump_json()
        self.answer.setText("<h2>Сохранено</h2>")

    def get_find_text(self):
        for self.car_data in self.car_json:
            if not self.request.text():
                self.answer.setText('<h2>Введите номер авто или часть номера</h2>')
            elif self.request.text() in self.car_data['number']:
                text_print = f'<h3>{self.car_data["number"]} </h3>'
                for i in self.car_data['data']:
                    text_print += f"<h3>{i}\n<\h3>"
                self.answer.setText(text_print)
                break
            else:
                self.answer.setText('<h2>Нет такого автомобиля</h2>')

    def dump_json(self):
        with open("data.json", 'w') as file:
            json.dump(self.car_json, file, indent=4, ensure_ascii=False)





def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
