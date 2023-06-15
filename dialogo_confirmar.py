from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import os

def dialogo_confirmacion(mensaje):
    dialogo = QMessageBox()
    dialogo.setWindowTitle('Eliminar')
    dialogo.setWindowIcon(QIcon('imagenes/logx.jpg'))
    dialogo.setIcon(QMessageBox.Question)
    dialogo.setText(mensaje)
    dialogo.addButton(QMessageBox.Yes)
    dialogo.addButton(QMessageBox.No)

    resultado = dialogo.exec()

    if resultado == QMessageBox.Yes:
        carrito = open('carrito.txt')
        carrito_suma = []
        total = 0

        for producto in carrito:
            carrito_suma.append(int(producto.strip().split()[3]))

        for producto in carrito_suma:
            total += producto

        todo_ = open('total.txt', 'w')
        todo_.write(f'Total productos: {str(total)}')

        carrito.close()
        todo_.close()