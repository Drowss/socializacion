from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QComboBox, \
    QSpinBox, QPushButton
from dialogo import dialogo
from pathlib import Path
import os
class Modificar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Modificacion producto')
        self.layout = QFormLayout()
        self.setStyleSheet("background-color:white;")

        self.setWindowIcon(QIcon("imagenes/logx.jpg"))

        self.ancho = 500
        self.alto = 200

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

        self.categoria_producto = QLabel('Producto a modificar')
        self.categoria_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.producto = QComboBox()
        self.producto.addItem('Seleccione un producto a modificar')
        self.producto.setFixedWidth(200)

        for productos in Path('productos_tienda').glob('**/*.txt'):
            productos = str(productos)
            self.producto.addItem(productos.replace('.txt','').replace('productos_tienda\\','').replace('_',' '))

        self.producto.currentIndexChanged.connect(self.holder)

        self.layout.addRow(self.categoria_producto, self.producto)

        self.nombre_producto = QLabel('Modificar nombre')
        self.nombre_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.nombre_producto1 = QLineEdit()
        self.nombre_producto1.setFixedWidth(200)

        self.layout.addRow(self.nombre_producto, self.nombre_producto1)

        self.cantidades_producto = QLabel('Modificar existencias')
        self.cantidades_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.cantidades_producto1 = QSpinBox()
        self.cantidades_producto1.setFixedWidth(100)
        self.cantidades_producto1.setRange(1,20)
        self.cantidades_producto1.setSuffix(' unidad(es)')

        self.layout.addRow(self.cantidades_producto, self.cantidades_producto1)

        self.precio_producto = QLabel('Modificar valor')
        self.precio_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.precio_producto1 = QLineEdit()
        self.precio_producto1.setFixedWidth(200)

        self.layout.addRow(self.precio_producto, self.precio_producto1)

        self.tamano_producto = QLabel('Modificar tamaño')
        self.tamano_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.tamano_producto1 = QComboBox()
        self.tamano_producto1.setFixedWidth(200)
        self.tamano_producto1.addItems(['375 ml (Media)', '750 ml (Botella)'])

        self.layout.addRow(self.tamano_producto, self.tamano_producto1)

        self.editar = QPushButton('Editar')
        self.editar.setFixedWidth(160)
        self.editar.setStyleSheet("""
                    QPushButton {
                        background-color: #e9f0e5;
                        border-radius: 15px;
                        padding: 10px 20px;
                        color: black;
                        font-size: 16px;
                        border: 2px solid #e9f0e5;
                        }
                    QPushButton:hover {
                        background-color: #e5d6d7;
                        }
                    QPushButton:pressed {
                            background-color: #fff0b1;
        
                        }
                    """)
        self.editar.clicked.connect(self.edicion_finalizada)
        self.layout.addWidget(self.editar)

        self.fondo.setLayout(self.layout)


    def edicion_finalizada(self):
        validar = True

        if self.nombre_producto1.text() == '' or self.precio_producto1.text() == '':
            dialogo('No ingresaste todos los datos requeridos.', 'no')
            validar = False

        elif not self.nombre_producto1.text().replace(' ', '').isalpha() or not self.precio_producto1.text().replace('.', '').isnumeric():
            dialogo('Los nombres deben ser escritos en carácteres y/o los precios numéricos', 'no')
            validar = False

        if validar:
            archivo1 = open(f'productos_tienda\\{self.producto.currentText().replace(" ", "_")}.txt')
            categoria = eval(archivo1.read())[0]
            archivo1.close()
            archivo = open(f'productos_tienda\\{self.producto.currentText().replace(" ", "_")}.txt', 'w')
            info_producto_actualizado = f'{categoria} {self.nombre_producto1.text().replace(" ", "_")} {self.cantidades_producto1.value()} {self.precio_producto1.text()} {self.tamano_producto1.currentText().replace(" ", "_")}'
            archivo.write(str(info_producto_actualizado.split()))
            archivo.close()
            os.rename(f'productos_tienda\\{self.producto.currentText().replace(" ", "_")}.txt', f'productos_tienda\\{self.nombre_producto1.text().replace(" ", "_")}.txt')
            self.close()

    def holder(self):
        if self.producto.currentText() == 'Seleccione un producto a modificar':
            self.nombre_producto1.setEnabled(False)
            self.precio_producto1.setEnabled(False)
            self.nombre_producto1.setPlaceholderText('')
            self.precio_producto1.setPlaceholderText('')
            self.cantidades_producto1.hide()
            self.tamano_producto1.setEnabled(False)
        elif not self.producto.currentText() == 'Seleccione un producto a modificar':
            archivo = open(f'productos_tienda\\{self.producto.currentText().replace(" ", "_")}.txt')
            lista = eval(archivo.read())
            self.nombre_producto1.setPlaceholderText(self.producto.currentText())
            self.precio_producto1.setPlaceholderText(lista[3])
            archivo.close()
            self.producto.setEnabled(True)
            self.nombre_producto1.setEnabled(True)
            self.precio_producto1.setEnabled(True)
            self.cantidades_producto1.show()
            self.tamano_producto1.setEnabled(True)