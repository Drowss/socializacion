from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QComboBox, \
    QSpinBox, QPushButton
from dialogo import dialogo
from pathlib import Path
import os
from dialogo_confirmar import dialogo_confirmacion
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

        self.confirmar = QPushButton('Comprar')
        self.confirmar.setStyleSheet("""
            QPushButton {
                background-color: #e9f0e5;
                border-radius: 15px;
                padding: 10px 20px;
                color: black;
                font-size: 16px;
                border: 2px solid #e9f0e5;
                margin-top: 40px;
                }
            QPushButton:hover {
                background-color: #e5d6d7;
                }
            QPushButton:pressed {
                    background-color: #fff0b1;

                }
            """)
        self.confirmar.clicked.connect(self.confirmar_compra)

        self.totales = QLabel()
        self.totales.setStyleSheet("background-color:transparent; color:#fff0b1;")
        self.totales.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))

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

        self.layout.addWidget(self.confirmar)
        self.layout.addWidget(self.totales)
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

    def confirmar_compra(self):
        Message = dialogo(self)
        resultado = Message.exec_()

        if resultado == QMessageBox.Yes:
            carrito = open('carrito.txt')
            carrito_suma = []
            total = 0

            for producto in carrito:
                indice_vigilante = 0
                while not producto.strip().split()[indice_vigilante].isnumeric():
                    indice_vigilante += 1
                    if producto.strip().split()[indice_vigilante].isnumeric():
                        carrito_suma.append(int(producto.strip().split()[indice_vigilante]))

            for producto in carrito_suma:
                total += producto

            todo_ = open('total.txt', 'w')
            todo_.write(f'Total productos: {str(total)}')
            todo_.close()
            todo_ = open('total.txt', 'r')
            self.totales.setText(todo_.read().replace('Total productos: ', 'Total productos: \n') + todo_.read().replace('Total productos: ', ''))

            carrito.close()




from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import os

class dialogo(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Eliminar')
        self.setWindowIcon(QIcon('imagenes/logx.jpg'))
        self.setIcon(QMessageBox.Question)
        self.setText('Esta seguro de confirmar la compra?')
        self.addButton(QMessageBox.Yes)
        self.addButton(QMessageBox.No)


