import os

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QToolBar, QAction, QLabel, QComboBox, QPushButton
from persona_encargadx import persona_a_cargo
from crear_producto import creacion_producto
from pathlib import Path
from modificacion_producto import Modificar
from eliminar_productos import Eliminar
class Ventana_pedido(QMainWindow):
    def __init__(self):
        super().__init__()
        self.disabled = """
                        QPushButton {
                            background-color: #3A383E;
                            border-radius: 15px;
                            padding: 10px 20px;
                            color: black;
                            font-size: 16px;
                            border: 2px solid #e9f0e5;
                            }
                        QPushButton:hover {
                            background-color: #4BC535;
                            }
                        QPushButton:pressed {
                                background-color: #39A426;

                            }
                        """

        self.enabled = """
                            QPushButton {
                                background-color: #5EFF42;
                                border-radius: 15px;
                                padding: 10px 20px;
                                color: black;
                                font-size: 16px;
                                border: 2px solid #e9f0e5;
                                }
                            QPushButton:hover {
                                background-color: #4BC535;
                                }
                            QPushButton:pressed {
                                    background-color: #39A426;

                                }
                            """

        self.setWindowTitle('Toma de pedido')

        self.setStyleSheet("background-color:white;")

        self.setWindowIcon(QIcon("imagenes/logx.jpg"))

        self.ancho = 650
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagenes/nirv1.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.setCentralWidget(self.fondo)

        self.bar = QToolBar()
        self.bar.setStyleSheet("background-color: gray")
        self.bar.setMovable(False)
        self.perfil = QAction(QIcon('imagenes/user.png'), 'Perfil', self)
        self.carrito = QAction(QIcon('imagenes/carrito.png'), 'Carrito', self)
        self.perfil.triggered.connect(self.encargadx)
        self.bar.addAction(self.perfil)
        self.bar.addAction(self.carrito)
        self.addToolBar(self.bar)


        self.precios = QLabel("Elige un producto", self)
        self.precios.setFixedWidth(340)
        self.precios.setFixedHeight(70)
        self.precios.setStyleSheet("border-radius: 10px; background-color: rgba(255, 196, 93, 50); color:#FFFFFF;")
        self.precios.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.precios.move(300, 110)

        self.productos_visuales()

        self.boton = QPushButton('Añadir al carrito', self)
        self.boton.setFixedSize(300,80)
        self.boton.setStyleSheet(self.disabled)
        self.boton.setEnabled(False)
        self.boton.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.boton.move(300,400)

        self.creacion = QPushButton('Crear producto', self)
        self.creacion.setFixedSize(170, 50)
        self.creacion.setStyleSheet(self.enabled)
        self.creacion.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.creacion.clicked.connect(self.crear)
        self.creacion.move(60, 500)

        self.modificar = QPushButton('Modificar producto', self)
        self.modificar.setFixedSize(170, 50)
        self.modificar.setStyleSheet(self.enabled)
        self.modificar.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.modificar.clicked.connect(self.modificar_producto)
        self.modificar.move(260, 500)

        self.eliminar_plano = QPushButton('Eliminar producto', self)
        self.eliminar_plano.setFixedSize(170, 50)
        self.eliminar_plano.setStyleSheet(self.enabled)
        self.eliminar_plano.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.eliminar_plano.clicked.connect(self.eliminar_producto)
        self.eliminar_plano.move(460, 500)

        self.productos.currentIndexChanged.connect(self.precio)


    def crear(self):
        self.crea = creacion_producto()
        self.crea.show()

    def encargadx(self):
        self.a_cargo = persona_a_cargo()
        self.a_cargo.show()

    def opcion(self):
        if self.media.isChecked():
            self.botella.setChecked(False)
        elif self.botella.isChecked():
            self.media.setChecked(False)


    def desmarcar(self):
        self.botella.setChecked(False)
        self.media.setChecked(False)

    def check_botella(self):
        pass
    def check_media(self):
        pass

    def precio(self):
        if self.productos.currentText() == 'Selecciona un producto':
            self.precios.setText('Selecciona un producto')
            self.boton.setEnabled(False)
            self.boton.setStyleSheet(self.disabled)
        elif not self.productos.currentText() == 'Selecciona un producto':
            archivo = open('productos_tienda/' + self.productos.currentText().replace("\n","").replace(" ", "_") + '.txt')
            lista_archivo = eval(archivo.read())
            self.precios.setText(f' Precio de {self.productos.currentText()} {lista_archivo[4].replace("_"," ")}\n {lista_archivo[3]} pesos, {lista_archivo[2]} unidad/es restantes')
            archivo.close()
            self.boton.setEnabled(True)
            self.boton.setStyleSheet(self.enabled)


    def tamano(self):
        pass



    def modificar_producto(self):
        self.modificacion = Modificar()
        self.modificacion.show()

    def productos_visuales(self):
        self.productos = QComboBox(self)
        self.productos.addItem('Selecciona un producto')
        productos = open('productos.txt','w')
        for producto in Path('productos_tienda').glob('**/*.txt'):
            producto_str = str(producto)
            producto_str2 = producto_str.replace("productos_tienda\\","").replace(".txt","")
            productos.write(f'{producto_str2}\n')
        productos.close()
        self.productividad = open('productos.txt')

        for producto in self.productividad:
            producto.strip()
            self.productos.addItem(producto.replace('_',' '))

        self.productividad.close()

        self.productos.setFixedWidth(200)
        self.productos.move(70,100)

    def eliminar_producto(self):
        self.eliminacion = Eliminar()
        self.eliminacion.show()