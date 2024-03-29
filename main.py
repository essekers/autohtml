# -*- coding: utf-8 -*-

# sys нужен для передачи argv в QApplication
import sys

# Отсюда нам понадобятся методы для отображения содержимого директорий
import os

import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QTextEdit, QApplication
from PyQt5.QtGui import QIcon, QClipboard

# Это наш конвертированный файл дизайна
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()

        # Это нужно для инициализации нашего дизайна
        self.setupUi(self)

        self.addToClipBoard()

        # Кнопка для верстки текста
        self.pushButton_2.clicked.connect(self.verstat)

    def verstat(self):

        # Передаем в переменную text то что пользователь ввел в поле
        textUser = self.textEdit.toPlainText()

        text = textUser.split('\n')

        for textline in text:
            if textline.find('#1 ') != -1:
                textline = f'<h1>{textline}</h1>\n'
            elif textline.find('#2 ') != -1:
                textline = f'<h2>{textline}</h2>\n'
            elif textline.find('#3 ') != -1:
                textline = f'<h3>{textline}</h3>\n'
            elif textline.find('#4 ') != -1:
                textline = f'<h4>{textline}</h4>\n'
            elif textline.find('* ') != -1:
                textline = f'<li>{textline}</li>\n'
            else:
                textline = f'<p>{textline}</p>\n'

            textline = re.sub(r'#..|[*].', r'', textline)
            textline = re.sub(r'(\<li\>(.*?)\<\/li\>*)+', f'<ul>\n{textline}</ul>' ,textline)

            self.textEdit_2.insertPlainText(textline)

    def addToClipBoard(self):
        self.pushButton_3.clicked.connect(self.ClipBoard)

    def ClipBoard(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.textEdit_2.toPlainText(), mode=cb.Clipboard)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
