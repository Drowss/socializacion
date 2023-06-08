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
        self.layout = QFormLayout()
        self.setStyleSheet("background-color:white;")

        self.setWindowIcon(QIcon("imagenes/logx.jpg"))

        self.ancho = 500
        self.alto = 700

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
        self.setLayout(self.layout)

        self.productos = []
        self.botones = []
        self.layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        for i, producto_carrito in enumerate(open('carrito.txt')):
            item = QLabel(producto_carrito.strip())
            item.setStyleSheet("background-color:transparent; color:#fff0b1;")
            item.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))

            boton = QPushButton(icon=QIcon('imagenes/delete.png.png'))
            boton.setFixedWidth(40)
            boton.clicked.connect(lambda _, idx=i: self.delete(idx))

            self.layout.addRow(item, boton)

            self.productos.append(item)
            self.botones.append(boton)

        self.fondo.setLayout(self.layout)

    def delete(self, idx):
        producto = self.productos[idx]
        boton = self.botones[idx]

        producto_text = producto.text()
        with open('carrito.txt', 'r') as file:
            lines = file.readlines()

        with open('carrito.txt', 'w') as file:
            eliminado = False
            for line in lines:
                if line.strip() == producto_text and not eliminado:
                    eliminado = True
                else:
                    file.write(line)

        producto.setParent(None)
        boton.setParent(None)
