from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import os

def dialogo_eliminar(mensaje):
    dialogo = QMessageBox()
    dialogo.setWindowTitle('¡Oops!')
    dialogo.setWindowIcon(QIcon('imagenes/logx.jpg'))
    dialogo.setIcon(QMessageBox.Question)
    dialogo.setText(mensaje)
    dialogo.addButton(QMessageBox.Yes)
    dialogo.addButton(QMessageBox.No)

    resultado = dialogo.exec()

    if resultado == QMessageBox.Yes:
        os.remove(f'productos_tienda\\{mensaje.replace("¿Estás seguro de eliminar ", "").replace("?","").replace(" ","_")}.txt')
