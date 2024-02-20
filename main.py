from PySide6.QtWidgets import QLineEdit, QWidget, QApplication, QMessageBox, QPushButton
from PySide6.QtGui import QCloseEvent, QIntValidator
import random
import string
import os

class Aplikacja(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(480, 360)
        self.setWindowTitle("Generator")
        self.run()
    def run(self):

        self.liczba = QIntValidator()

        self.TAG = QLineEdit(self)
        self.TAG.setPlaceholderText("Wpisz TAG")
        self.TAG.move(80, 130)

        self.road = QLineEdit(self)
        self.road.setText("C:\\generator\\Notatnik.txt")
        self.road.setPlaceholderText("Podaj sciezke zapisu")
        self.road.move(220, 130)
        self.road.setFixedSize(250, 20)

        self.line = QLineEdit(self)
        self.line.setValidator(self.liczba)
        self.line.setPlaceholderText("Oczekiwana dlugosc hasla/ciagu cyfr")
        self.line.move(130, 160)
        self.line.resize(220, 20)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Generuj haslo")
        self.btn1.move(120, 190)
        self.btn1.clicked.connect(self.haslo)

        self.btn2 = QPushButton(self)
        self.btn2.setText("Generuj ciag")
        self.btn2.move(240, 190)
        self.btn2.clicked.connect(self.ciag)

        self.btnq = QPushButton(self)
        self.btnq.setText("Wyjscie")
        self.btnq.move(400, 330)
        self.btnq.clicked.connect(QApplication.instance().quit)



        self.show()


    def closeEvent(self, event: QCloseEvent):
        zamkniecie = QMessageBox.question(self, "Zamykanie aplikacji", "Czy chcesz zamknac aplikacje?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if zamkniecie == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    def haslo(self):
        dlugosc = int(self.line.text())
        chars = string.ascii_letters + string.digits
        z ="".join(random.choice(chars) for _ in range(dlugosc))
        os.path = self.road.text()
        os.access("C:\\", os.W_OK)
        plik = open(os.path, "a")
        plik.write("----------------------\n")
        plik.write(self.TAG.text())
        plik.write("\n")
        plik.write(z)
        plik.write("\n")
        plik.write("----------------------\n")
        plik.write("\n")

    def ciag(self):
        dlugosc = int(self.line.text())
        chars = string.ascii_letters 
        c ="".join(random.choice(chars) for _ in range(dlugosc))
        os.path = self.road.text()
        os.access("C:\\", os.W_OK)
        plik = open(os.path, "a")
        plik.write("----------------------\n")
        plik.write(self.TAG.text())
        plik.write("\n")
        plik.write(c)
        plik.write("\n")
        plik.write("----------------------\n")
        plik.write("\n")





app = QApplication([])
aplikacja = Aplikacja()
app.exec()