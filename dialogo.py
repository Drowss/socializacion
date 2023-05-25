from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


def dialogo(mensaje):
    dialogo = QMessageBox()
    dialogo.setWindowTitle('¡Oops!')
    dialogo.setWindowIcon(QIcon('imagenes/logx.jpg'))
    dialogo.setText(mensaje)
    dialogo.exec()