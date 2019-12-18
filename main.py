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
        text = self.textEdit.toPlainText()

        openfile = 'QTextDocument.txt'

        # Создаем текстовый документ
        fSave = open(openfile, 'w')

        # записывем в файл текст
        fSave.write(text)

        # Закрываем файл
        fSave.close()

        with open(openfile) as f:
            content = f.readlines()

        with open(openfile, 'w') as f:
            for line in content:
                f.write('<p>' + line.strip() + '</p>\n')

        with open(openfile, 'r') as f:
            old_text = f.read()

        new_text = old_text\
            .replace('<p><p>', '<p>').replace('</p></p>', '</p>')

        with open(openfile, 'w') as f:
            f.write(new_text)

        textOpen = open(openfile)

        self.textEdit_2.insertPlainText(textOpen.read())

        textOpen.close()

# self.textEdit_2.setText(a) # Выводим текст пользователя в колонку результат

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
