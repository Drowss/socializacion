from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QComboBox, \
    QSpinBox, QPushButton, QMessageBox
from dialogo_eliminacion import dialogo_eliminar
from pathlib import Path
import os
class Eliminar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eliminar producto')
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

        self.eliminar_producto = QLabel('Producto a eliminar')
        self.eliminar_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')

        self.producto = QComboBox()
        self.producto.addItem('Seleccione un producto a eliminar')
        self.producto.setFixedWidth(200)

        for productos in Path('productos_tienda').glob('**/*.txt'):
            productos = str(productos)
            self.producto.addItem(productos.replace('.txt','').replace('productos_tienda\\','').replace('_',' '))

        self.producto.currentIndexChanged.connect(self.producto_a_eliminar)

        self.layout.addRow(self.eliminar_producto, self.producto)

        self.boton_eliminar = QPushButton('Eliminar producto')
        self.boton_eliminar.setFixedWidth(190)
        self.boton_eliminar.setEnabled(False)
        self.boton_eliminar.setStyleSheet("""
                    QPushButton {
                        background-color: #3A383E;
                        border-radius: 15px;
                        padding: 10px 20px;
                        color: black;
                        font-size: 16px;
                        border: 2px solid #e9f0e5;
                        margin-top: 90px
                        }
                    QPushButton:hover {
                        background-color: #4BC535;
                        }
                    QPushButton:pressed {
                            background-color: #39A426;

                        }
                    """)
        self.boton_eliminar.clicked.connect(self.eliminacion_confirmada)
        self.layout.addWidget(self.boton_eliminar)

        self.fondo.setLayout(self.layout)

    def producto_a_eliminar(self):
        if self.producto.currentText() == 'Seleccione un producto a eliminar':
            self.boton_eliminar.setEnabled(False)
            self.boton_eliminar.setStyleSheet("""
                        QPushButton {
                            background-color: #3A383E;
                            border-radius: 15px;
                            padding: 10px 20px;
                            color: black;
                            font-size: 16px;
                            border: 2px solid #e9f0e5;
                            margin-top: 90px
                            }
                        QPushButton:hover {
                            background-color: #4BC535;
                            }
                        QPushButton:pressed {
                                background-color: #39A426;

                            }
                        """)

        if not self.producto.currentText() == 'Seleccione un producto a eliminar':
            self.boton_eliminar.setEnabled(True)
            self.boton_eliminar.setStyleSheet("""
                            QPushButton {
                                background-color: #5EFF42;
                                border-radius: 15px;
                                padding: 10px 20px;
                                color: black;
                                font-size: 16px;
                                border: 2px solid #e9f0e5;
                                margin-top: 90px
                                }
                            QPushButton:hover {
                                background-color: #4BC535;
                                }
                            QPushButton:pressed {
                                    background-color: #39A426;

                                }
                            """)

    def eliminacion_confirmada(self):
        dialogo_eliminar(f'¿Estás seguro de eliminar {self.producto.currentText()}?')
