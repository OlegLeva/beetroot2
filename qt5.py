import sys
from functools import partial

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
        self.editArea = QLineEdit('0')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.editArea)

        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': '1',
                'row': 0,
                'col': 0
            },
            {
                'name': '2',
                'row': 0,
                'col': 1
            },
            {
                'name': '3',
                'row': 0,
                'col': 2
            },
            {
                'name': '4',
                'row': 1,
                'col': 0
            },
            {
                'name': '5',
                'row': 1,
                'col': 1
            },
            {
                'name': '6',
                'row': 1,
                'col': 2
            },
            {
                'name': '7',
                'row': 2,
                'col': 0
            },
            {
                'name': '8',
                'row': 2,
                'col': 1
            },
            {
                'name': '9',
                'row': 2,
                'col': 2
            },
            {
                'name': '0',
                'row': 3,
                'col': 0,
                'colSpan': 3
            }
        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig.get('row', -1),
                                   buttonConfig.get('col', -1),
                                   1,
                                   buttonConfig.get('colSpan', 1))
        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        for buttonName in self.buttons:
            btn = self.buttons[buttonName]
            btn.clicked.connect(partial(self.change_text, buttonName))

    def change_text(self, text):
        self.editArea.setText(self.editArea.text() + text)


def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
