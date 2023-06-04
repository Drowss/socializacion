from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QPushButton


class persona_a_cargo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Encargado(a)')
        self.layout = QVBoxLayout()
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

        datos_encargado = open('encargado.txt')
        usuario_datos = eval(datos_encargado.read())
        self.nombre_encargado = QLabel(f"Nombre del encargado: {usuario_datos[0].replace('_', ' ')}", self)
        self.nombre_encargado.setStyleSheet("background-color:transparent; color:#fff0b1;")
        self.nombre_encargado.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.layout.addWidget(self.nombre_encargado)

        self.correo_encargado = QLabel(f"Correo del encargado: {usuario_datos[2]}", self)
        self.correo_encargado.setStyleSheet("background-color:transparent; color:#fff0b1;")
        self.correo_encargado.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.layout.addWidget(self.correo_encargado)

        self.numero_encargado = QLabel(f"Número telefónico del encargado: {usuario_datos[4]}", self)
        self.numero_encargado.setStyleSheet("background-color:transparent; color:#fff0b1;")
        self.numero_encargado.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.layout.addWidget(self.numero_encargado)

        datos_encargado.close()

        self.salida = QPushButton('Cerrar')
        self.salida.setFixedWidth(100)
        self.salida.setStyleSheet("""
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
        self.salida.clicked.connect(self.cerrar)
        self.layout.addWidget(self.salida)


        self.fondo.setLayout(self.layout)

    def cerrar(self):
        self.close()
