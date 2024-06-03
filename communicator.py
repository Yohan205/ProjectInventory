from PyQt5.QtCore import pyqtSignal, QObject

# Definir una clase para manejar señales personalizadas
class Communicator(QObject):
    # Definir una señal que lleva un string
    updateAlertBox = pyqtSignal(str)