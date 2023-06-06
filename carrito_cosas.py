from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QComboBox, \
    QSpinBox, QPushButton
from dialogo import dialogo
from pathlib import Path
import os
class Carrito_ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Carrito')
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet("background-color:white;")

        self.setWindowIcon(QIcon("imagenes/logx.jpg"))

        self.ancho = 700
        self.alto = 1000

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/fondoazul.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.setCentralWidget(self.fondo)

        for producto_carrito in open('carrito.txt'):
            item = QLabel(producto_carrito)
            item.setStyleSheet("background-color:transparent; color:#fff0b1;")
            item.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
            item.setFixedHeight(20)
            self.layout.addWidget(item)

        self.fondo.setLayout(self.layout)