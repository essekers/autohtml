# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QTextEdit, QApplication
from PyQt5.QtGui import QIcon, QClipboard

import design  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.addToClipBoard()
        self.pushButton_2.clicked.connect(self.verstat) # Кнопка для верстки текста

    def verstat(self):

        text = self.textEdit.toPlainText() # Передаем в переменную text то что пользователь ввел в поле

        fSave = open('QTextDocument.txt', 'w') # Создаем текстовый документ
        fSave.write(text) # записывем в файл текст
        fSave.close() # Закрываем файл

        with open('QTextDocument.txt') as f:
            content = f.readlines()

        with open('QTextDocument.txt', 'w') as f:
            for line in content:
                f.write('<p>' + line.strip() + '</p>\n')

        with open ('QTextDocument.txt', 'r') as f:
            old_text = f.read()

        new_text = old_text\
        .replace('<p><p>', '<p>')\
        .replace('</p></p>', '</p>')


        with open ('QTextDocument.txt', 'w') as f:
            f.write(new_text)

        textOpen = open('QTextDocument.txt')


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
