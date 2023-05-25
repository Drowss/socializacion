from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QToolBar, QAction, QLabel, QComboBox, QPushButton


class Ventana_pedido(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toma de pedido")

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
        self.bar.addAction(self.perfil)
        self.bar.addAction(self.carrito)
        self.addToolBar(self.bar)


        self.precios = QLabel("Elige un producto", self)
        self.precios.setFixedWidth(340)
        self.precios.setFixedHeight(70)
        self.precios.setStyleSheet("border-radius: 10px; background-color: rgba(255, 196, 93, 50); color:#FFFFFF;")
        self.precios.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.precios.move(300, 110)

        self.media = QPushButton('375ml (Media)', self)
        self.media.setEnabled(False)
        self.media.setFixedSize(160, 40)
        self.media.setStyleSheet("""
                    QPushButton {
                        background-color: #3A383E;
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
        self.media.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.media.move(300, 200)

        self.botella = QPushButton('750ml (Botella)', self)
        self.botella.setFixedSize(160, 40)
        self.botella.setEnabled(False)
        self.botella.setStyleSheet("""
                    QPushButton {
                        background-color: #3A383E;
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
        self.botella.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.botella.move(470, 200)

        self.categoria = QComboBox(self)
        self.categoria.setFixedWidth(200)
        self.categoria.move(70, 100)
        self.categoria.addItem('Seleccione categoría')
        self.categoria.addItem('Cerveza')
        self.categoria.addItem('Alcohol tradicional')
        self.categoria.addItem('Vodka')
        self.categoria.currentIndexChanged.connect(self.categorias)

        self.licores = QComboBox(self)
        self.licores.setFixedWidth(200)
        self.licores.move(70, 190)
        self.licores.hide()
        self.licores.addItem('Seleccione su producto')
        #self.licores.addItem('Aguardiente (Tapa roja)')
        #self.licores.addItem('Aguardiente (Tapa azul)')
        #self.licores.addItem('Aguila')
        #self.licores.addItem('Ron viejo de Caldas (Tradicional)')
        #self.licores.addItem('Pilsen')
        self.licores.currentIndexChanged.connect(self.precio)
        self.licores.currentIndexChanged.connect(self.desmarcar)
        self.licores.currentIndexChanged.connect(self.tamano)

        #self.media.clicked.connect(self.opcion)
        self.media.clicked.connect(self.check_media)

        #self.botella.clicked.connect(self.opcion)
        self.botella.clicked.connect(self.check_botella)


        self.boton = QPushButton('Añadir al carrito', self)
        self.boton.setFixedSize(300,80)
        self.boton.setStyleSheet("""
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
            """)
        self.boton.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.boton.move(300,400)



    def categorias(self):
        if self.categoria.currentText() == 'Seleccione categoría':
            self.boton.setStyleSheet("""
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
                            """)
            self.boton.setEnabled(False)
        else:
            self.boton.setStyleSheet("""
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
                            """)
            self.boton.setEnabled(True)

        match self.categoria.currentText():
            case 'Seleccione categoría':
                self.licores.hide()
                self.precios.setText(f" Selecciona una categoría")

            case 'Cerveza':
                self.licores.show()
                self.licores.clear()
                self.licores.addItem('Aguila')
                self.licores.addItem('Pilsen')
                self.boton.show()

            case 'Alcohol tradicional':
                self.licores.show()
                self.licores.clear()
                self.licores.addItem('Aguardiente (Tapa roja)')
                self.licores.addItem('Aguardiente (Tapa azul)')
                self.licores.addItem('Ron viejo de Caldas (Tradicional)')
                self.boton.show()

            case 'Vodka':
                self.licores.show()
                self.licores.clear()
                self.licores.addItem('Absolut Vodka 1 Litro')
                self.licores.addItem('Smirnoff Vodka 700ml')
                self.boton.show()


    def opcion(self):
        if self.media.isChecked():
            self.botella.setChecked(False)
        elif self.botella.isChecked():
            self.media.setChecked(False)


    def desmarcar(self):
        self.botella.setChecked(False)
        self.media.setChecked(False)

    def check_botella(self):
        if self.botella.isChecked():
            self.botella.setStyleSheet("""
                QPushButton {
                    background-color: #12848B;
                    border-radius: 15px;
                    padding: 10px 20px;
                    color: black;
                    font-size: 16px;
                    border: 2px solid #e9f0e5;
                    }
                QPushButton:hover {
                    background-color: #0B4A4E;
                    }
            """)
            self.media.setChecked(False)

        if self.media.isChecked() == False:
            self.media.setStyleSheet("""
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
            """)
        if self.botella.isChecked() == False:
            self.botella.setStyleSheet("""
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
            """)
    def check_media(self):
        if self.media.isChecked():
            self.media.setStyleSheet("""
                QPushButton {
                    background-color: #12848B;
                    border-radius: 15px;
                    padding: 10px 20px;
                    color: black;
                    font-size: 16px;
                    border: 2px solid #e9f0e5;
                    }
                QPushButton:hover {
                    background-color: #0B4A4E;
                    }
            """)
            self.botella.setChecked(False)

        if self.media.isChecked() == False:
            self.media.setStyleSheet("""
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
            """)
        if self.botella.isChecked() == False:
            self.botella.setStyleSheet("""
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
            """)

    def precio(self):
        match self.licores.currentText():
            case 'Aguardiente (Tapa roja)':
                self.precios.setText(f' Precio de {self.licores.currentText()}\n 375 ml 21.000$\n 750 ml 39.000$')
                self.botella.show()
                self.media.show()
            case 'Aguardiente (Tapa azul)':
                self.precios.setText(f' Precio de {self.licores.currentText()}\n 375 ml 23.000$\n 750 ml 42.000$')
                self.botella.show()
                self.media.show()
            case 'Aguila':
                self.precios.setText(f' Precio de cerveza {self.licores.currentText()}\n 3500 c/u')
                self.botella.hide()
                self.media.hide()
            case 'Ron viejo de Caldas (Tradicional)':
                self.precios.setText(f' Precio de {self.licores.currentText()}\n 375 ml 26.000$\n 750 ml 48.000$')
                self.botella.show()
                self.media.show()
            case 'Pilsen':
                self.precios.setText(f' Precio de cerveza {self.licores.currentText()}\n 3500 c/u')
                self.botella.hide()
                self.media.hide()
            case 'Absolut Vodka 1 Litro':
                self.precios.setText(f' Precio de {self.licores.currentText()}\n 1 Litro 125.900$')
                self.media.hide()
                self.botella.hide()
            case 'Smirnoff Vodka 700ml':
                self.precios.setText(f' Precio de {self.licores.currentText()}\n 700 ml 107.900$')
                self.botella.hide()
                self.media.hide()


    def tamano(self):
        match self.licores.currentText():
            case 'Aguardiente (Tapa roja)':
                self.media.setStyleSheet("""
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
                            """)
                self.media.setEnabled(True)
                self.botella.setStyleSheet("""
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
                            """)
                self.botella.setEnabled(True)
                self.botella.setCheckable(True)
                self.media.setCheckable(True)
            case 'Aguardiente (Tapa azul)':
                self.media.setStyleSheet("""
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
                            """)
                self.media.setEnabled(True)
                self.botella.setStyleSheet("""
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
                            """)
                self.botella.setEnabled(True)
                self.botella.setCheckable(True)
                self.media.setCheckable(True)

            case 'Ron viejo de Caldas (Tradicional)':
                self.media.setStyleSheet("""
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
                            """)
                self.media.setEnabled(True)
                self.botella.setStyleSheet("""
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
                            """)
                self.botella.setEnabled(True)
                self.botella.setCheckable(True)
                self.media.setCheckable(True)








