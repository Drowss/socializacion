from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QComboBox, \
    QSpinBox, QPushButton
from dialogo import dialogo


class creacion_producto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Creación de producto')
        self.layout = QFormLayout()
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

        self.categoria_producto = QLabel('Categoría del producto')
        self.categoria_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.categoria = QComboBox()
        self.categoria.setFixedWidth(200)
        self.categoria.addItems(['Seleccione categoría', 'Cerveza', 'Alcohol tradicional', 'Vodka'])
        self.categoria.currentTextChanged.connect(self.categoria_del_producto)

        self.layout.addRow(self.categoria_producto, self.categoria)

        self.nombre_producto = QLabel('Nombre del producto')
        self.nombre_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.nombre_producto1 = QLineEdit()
        self.nombre_producto1.setEnabled(False)
        self.nombre_producto1.setFixedWidth(200)

        self.layout.addRow(self.nombre_producto, self.nombre_producto1)

        self.cantidades_producto = QLabel('¿Cuántas existencias?')
        self.cantidades_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.cantidades_producto1 = QSpinBox()
        self.cantidades_producto1.setFixedWidth(100)
        self.cantidades_producto1.setEnabled(False)
        self.cantidades_producto1.setRange(1,20)
        self.cantidades_producto1.setSuffix(' unidad(es)')

        self.layout.addRow(self.cantidades_producto, self.cantidades_producto1)

        self.precio_producto = QLabel('Valor del producto')
        self.precio_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.precio_producto1 = QLineEdit()
        self.precio_producto1.setEnabled(False)
        self.precio_producto1.setFixedWidth(200)

        self.layout.addRow(self.precio_producto, self.precio_producto1)

        self.tamano_producto = QLabel('Tamaño del producto')
        self.tamano_producto.setStyleSheet('background-color:transparent; color:#fff0b1;')
        self.tamano_producto1 = QComboBox()
        self.tamano_producto1.setFixedWidth(200)
        self.tamano_producto1.setEnabled(False)
        self.tamano_producto1.addItems(['375 ml (Media)', '750 ml (Botella)'])

        self.layout.addRow(self.tamano_producto, self.tamano_producto1)

        self.crear = QPushButton('Crear')
        self.crear.setFixedWidth(160)
        self.crear.setEnabled(False)
        self.crear.setStyleSheet("""
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
        self.crear.clicked.connect(self.creacion_confirmada)
        self.layout.addWidget(self.crear)



        self.fondo.setLayout(self.layout)

    def categoria_del_producto(self):
        if self.categoria.currentText() != 'Seleccione categoría':
            self.precio_producto1.setEnabled(True)
            self.cantidades_producto1.show()
            self.cantidades_producto1.setEnabled(True)
            self.nombre_producto1.setEnabled(True)
            self.tamano_producto1.setEnabled(True)
            self.crear.setEnabled(True)
            self.crear.setStyleSheet("""
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
        if self.categoria.currentText() == 'Seleccione categoría':
            self.precio_producto1.setEnabled(False)
            self.cantidades_producto1.setEnabled(False)
            self.nombre_producto1.setEnabled(False)
            self.tamano_producto1.setEnabled(False)
            self.crear.setEnabled(False)
            self.precio_producto1.setText('')
            self.cantidades_producto1.hide()
            self.nombre_producto1.setText('')
            self.crear.setStyleSheet("""
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

    def creacion_confirmada(self):
        validar = True
        if self.nombre_producto1.text() == '' or self.precio_producto1.text() == '':
            dialogo('No ingresaste todos los datos requeridos.')
            validar = False

        elif not self.nombre_producto1.text().replace(' ', '').isalpha() or not self.precio_producto1.text().replace('.', '').isnumeric():
            dialogo('Los nombres deben ser escritos en carácteres y/o los precios numéricos')
            validar = False


        if validar:
            producto = open(f'productos_tienda/{self.nombre_producto1.text().replace(" ", "_")}.txt', 'w')
            info_producto_nuevo = f'{self.categoria.currentText().replace(" ", "_")} {self.nombre_producto1.text().replace(" ", "_")} {self.cantidades_producto1.value()} {self.precio_producto1.text()} {self.tamano_producto1.currentText().replace(" ", "_")}'
            producto.write(str(info_producto_nuevo.split()))
            producto.close()
            self.close()

