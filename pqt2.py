from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QLabel, QLineEdit, QPushButton


class Registro_usuario(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.anterior = anterior

        self.setWindowTitle("Registro")

        #self.setStyleSheet("background-color:#f7dfd4;")

        self.setWindowIcon(QIcon("imagenes/logx.jpg"))

        self.ancho = 600
        self.alto = 800

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
        #self.fondo.setFixedSize(500,380)
        #self.fondo.move(40,400)
        self.setCentralWidget(self.fondo)

        self.user = QLabel("Usuario", self)
        self.user.setStyleSheet("background-color:transparent; color:#fff0b1;")
        self.user.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        #self.user.move(265, 90)
        self.user.move(260,85)

        self.user1 = QLineEdit(self)
        self.user1.setMaxLength(12)
        self.user1.setPlaceholderText('Máximo 12 carácteres')
        self.user1.setStyleSheet("""
                    QLineEdit {
                        background-color:#E0FFFF;
                        border-radius: 10px;
                        border: 2px solid #e9f0e5;
                        padding: 5px;
                    }
                    QLineEdit:hover {
                        background-color:#B0C4DE;
                    }
                    """)
        self.user1.setFixedWidth(160)
        self.user1.move(216, 120)

        self.pwd = QLabel("Contraseña", self)

        self.pwd.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.pwd.setStyleSheet("background-color:transparent;color: #fff0b1")
        self.pwd.move(250, 175)

        self.pwd1 = QLineEdit(self)
        self.pwd1.setMaxLength(12)
        self.pwd1.setPlaceholderText('Máximo 8 carácteres')
        self.pwd1.setEchoMode(QLineEdit.EchoMode.Password)
        self.pwd1.setStyleSheet("""
                    QLineEdit {
                        background-color:#E0FFFF;
                        border-radius: 10px;
                        border: 2px solid #e9f0e5;
                        padding: 5px;
                    }
                    QLineEdit:hover {
                        background-color:#B0C4DE;
                    }
                    """)
        self.pwd1.setFixedWidth(160)
        self.pwd1.move(216, 210)

        self.email = QLabel("Correo electrónico", self)
        self.email.setFixedWidth(163)
        self.email.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.email.setStyleSheet("background-color:transparent;color: #fff0b1")
        self.email.move(225, 265)

        self.email1 = QLineEdit(self)
        self.email1.setPlaceholderText('Ejemplo123@gmail.com')
        self.email1.setMaxLength(12)
        self.email1.setStyleSheet("""
                            QLineEdit {
                                background-color:#E0FFFF;
                                border-radius: 10px;
                                border: 2px solid #e9f0e5;
                                padding: 5px;
                            }
                            QLineEdit:hover {
                                background-color:#B0C4DE;
                            }
                            """)
        self.email1.setFixedWidth(160)
        self.email1.move(216, 300)
        
        self.cc = QLabel("Cédula de Ciudadanía", self)
        self.cc.setFixedWidth(163)
        self.cc.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.cc.setStyleSheet("background-color:transparent;color: #fff0b1")
        self.cc.move(215, 365)

        self.cc1 = QLineEdit(self)
        self.cc1.setMaxLength(12)
        self.cc1.setStyleSheet("""
                            QLineEdit {
                                background-color:#E0FFFF;
                                border-radius: 10px;
                                border: 2px solid #e9f0e5;
                                padding: 5px;
                            }
                            QLineEdit:hover {
                                background-color:#B0C4DE;
                            }
                            """)
        self.cc1.setFixedWidth(160)
        self.cc1.move(216, 400)

        self.boton = QPushButton("Crear Cuenta", self)
        self.boton.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.boton.setFixedSize(140, 40)
        #self.boton.clicked.connect(self.registro)
        self.boton.setStyleSheet("""
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

        self.boton.move(380, 550)

        self.boton = QPushButton("Cancelar", self)
        self.boton.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.boton.setFixedSize(140, 40)
        self.boton.clicked.connect(self.cancelar)
        self.boton.setStyleSheet("""
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

        self.boton.move(100, 550)

    def cancelar(self):
        self.hide()


