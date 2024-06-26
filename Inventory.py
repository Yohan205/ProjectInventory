import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4,155,180, 255), stop:1 rgba(125,216,87, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tittle = QtWidgets.QLabel(self.centralwidget)
        self.tittle.setGeometry(QtCore.QRect(210, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittle.setFont(font)
        self.tittle.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.tittle.setObjectName("tittle")
        self.eProduct = QtWidgets.QLabel(self.centralwidget)
        self.eProduct.setGeometry(QtCore.QRect(20, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.eProduct.setFont(font)
        self.eProduct.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.eProduct.setObjectName("eProduct")
        self.eCant = QtWidgets.QLabel(self.centralwidget)
        self.eCant.setGeometry(QtCore.QRect(120, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.eCant.setFont(font)
        self.eCant.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.eCant.setObjectName("eCant")
        self.eRef = QtWidgets.QLabel(self.centralwidget)
        self.eRef.setGeometry(QtCore.QRect(190, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.eRef.setFont(font)
        self.eRef.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.eRef.setObjectName("eRef")
        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(300, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.eTotal.setFont(font)
        self.eTotal.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.eTotal.setObjectName("eTotal")
        self.addSell = QtWidgets.QPushButton(self.centralwidget)
        self.addSell.setGeometry(QtCore.QRect(450, 150, 131, 41))
        self.addSell.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addSell.setStyleSheet("background-color: rgb(94, 23, 235);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 13pt \"Arial\";")
        self.addSell.setObjectName("addSell")
        self.reportDaily = QtWidgets.QPushButton(self.centralwidget)
        self.reportDaily.setGeometry(QtCore.QRect(460, 80, 121, 41))
        self.reportDaily.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportDaily.setStyleSheet("background-color: rgb(0, 151, 178);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 13pt \"Arial\";")
        self.reportDaily.setObjectName("reportDaily")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBack.setStyleSheet("background-color: rgb(126, 217, 87);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 13pt \"Arial\";")
        self.btnBack.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tittle.setText(_translate("MainWindow", "INFORME DEL DIA"))
        self.eProduct.setText(_translate("MainWindow", "Producto"))
        self.eCant.setText(_translate("MainWindow", "Cant."))
        self.eRef.setText(_translate("MainWindow", "Referencia"))
        self.eTotal.setText(_translate("MainWindow", "Total"))
        self.addSell.setText(_translate("MainWindow", "Agregar Venta"))
        self.reportDaily.setText(_translate("MainWindow", "Informe Diario"))
        self.btnBack.setText(_translate("MainWindow", "Atrás"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
