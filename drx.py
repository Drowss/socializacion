import sys
from pqt2 import Registro_usuario
from pedido import Ventana_pedido
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QApplication, QVBoxLayout, QLabel, QScrollArea, \
    QGridLayout, QButtonGroup, QPushButton, QLineEdit, QSystemTrayIcon


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent=parent)

        self.boton = QPushButton('click', self)
        self.boton.setCheckable(True)
        self.boton.clicked.connect(self.xd)


    def xd(self):
        if self.boton.isChecked():
            print('ala')
            self.boton.setStyleSheet('background-color: orange')
        elif self.boton.isChecked() == False:
            self.boton.setStyleSheet('background-color: green')
            print('ele')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())