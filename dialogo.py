from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


def dialogo(mensaje,pregunta):
    dialogo = QMessageBox()
    dialogo.setIcon(QMessageBox.Information)
    dialogo.setWindowTitle('¡Oops!')
    dialogo.setWindowIcon(QIcon('imagenes/logx.jpg'))
    dialogo.setText(mensaje)
    dialogo.exec()