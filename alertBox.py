from PyQt5 import QtCore, QtGui, QtWidgets


class AlertBox(QtWidgets.QDialog):
    def __init__(self, communicator, parent=None):
        super().__init__(parent)
        AlertBox = self
        AlertBox.setObjectName("AlertBox")
        AlertBox.resize(262, 189)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONOI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AlertBox.setWindowIcon(icon)
        AlertBox.setAutoFillBackground(False)
        AlertBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(130, 35, 233, 255), stop:1 rgba(162, 0, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(AlertBox)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(60, 110, 131, 41))
        self.btnNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNext.setStyleSheet("background-color: rgb(249, 167, 25);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.close)

        self.eAlerta = QtWidgets.QLabel(self.centralwidget)
        self.eAlerta.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eAlerta.setFont(font)
        self.eAlerta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"color: rgb(213, 0, 0);\n"
"border-radius:10px;")
        self.eAlerta.setObjectName("eAlerta")
        
        communicator.updateAlertBox.connect(self.setAlert)
        self.retranslateUi(AlertBox)
        
        # print("TXT Label: ",self.eAlerta.text())
        # QtCore.QMetaObject.connectSlotsByName(AlertBox)

    def retranslateUi(self, AlertBox):
        _translate = QtCore.QCoreApplication.translate
        AlertBox.setWindowTitle(_translate("AlertBox", "Alerta"))
        self.btnNext.setText(_translate("AlertBox", "Aceptar"))

    def setAlert(self, txt):
        # print("TXT AB:",txt)
        self.eAlerta.setText(txt)