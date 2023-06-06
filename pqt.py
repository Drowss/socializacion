import sys
from pqt2 import Registro_usuario
from pedido import Ventana_pedido
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QApplication, QVBoxLayout, QLabel, QScrollArea, \
    QGridLayout, QButtonGroup, QPushButton, QLineEdit, QSystemTrayIcon, QMessageBox
from dialogo import dialogo


##

class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent=parent)
        self.setWindowTitle("Licor Express")

        self.setStyleSheet("background-color:#f7dfd4;")
        self.setWindowIcon(QIcon("imagenes/logx.jpg"))

        self.ancho = 600
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

        #self.fondo.setFixedSize(self.ancho, self.alto)
        self.setCentralWidget(self.fondo)

        self.boton = QPushButton("Registrarse", self)
        self.boton.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.boton.setFixedSize(140, 40)
        self.user2 = self.boton.clicked.connect(self.registro)
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

        self.boton.move(100, 350)

        self.boton2 = QPushButton("Entrar", self)
        self.boton2.setFixedSize(120, 40)
        self.boton2.clicked.connect(self.entrar)
        self.boton2.setFont(QFont('Bahnschrift SemiLight SemiConde', 15))
        self.boton2.setStyleSheet("""
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

        self.boton2.move(380, 350)

        self.user = QLabel("Cédula", self)
        self.user.setStyleSheet("background-color:transparent; color:#fff0b1;")
        self.user.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.user.move(265, 90)

        self.user1 = QLineEdit(self)
        self.user1.setPlaceholderText('Ingrese su usuario')
        self.user1.setMaxLength(12)
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
        self.user1.returnPressed.connect(self.entrar)
        self.user1.setFixedWidth(160)
        self.user1.move(216, 120)

        self.pwd = QLabel("Contraseña", self)

        self.pwd.setFont(QFont("Bahnschrift SemiLight SemiConde", 15))
        self.pwd.setStyleSheet("background-color:transparent;color: #fff0b1")
        self.pwd.move(250, 190)

        self.pwd1 = QLineEdit(self)
        self.pwd1.setMaxLength(12)
        self.pwd1.setPlaceholderText('Ingrese su contraseña')
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
        self.pwd1.returnPressed.connect(self.entrar)
        self.pwd1.setFixedWidth(160)
        self.pwd1.move(216, 220)

    def registro(self):

        self.registro = Registro_usuario(self)
        self.registro.show()

    def entrar(self):
        archivo = open('usuarios.txt')
        validacion = True
        lista = []
        for usuario in archivo:
            valor = usuario.replace(';', ' ').split()
            lista.append(valor)

        for datos in lista:
            if datos[3] == self.user1.text() and datos[1] == self.pwd1.text():
                encargado = open('encargado.txt','w')
                encargado.write(str(datos))
                encargado.close()
                self.hide()
                self.entrar = Ventana_pedido()
                self.entrar.show()
                validacion = False


        if validacion:
            dialogo('Usuario y/o contraseña inválidos, asegúrese de introducir\ncorrectamente sus datos.', 'no')
        archivo.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())