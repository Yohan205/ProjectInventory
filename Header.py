import os
import sys
from datetime import datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

os.makedirs('ProjectInventory/DataBase', exist_ok=True)


class Inventory():
    def __init__(self):
        self.ref = []
        self.products = []
        self.cant = ""
        self.vlr = 0
        self.product = ""
        # slef

        app = QtWidgets.QApplication(sys.argv)
        InventoryHome = QtWidgets.QMainWindow()
        InventoryHome.setObjectName("InventoryHome")
        InventoryHome.resize(600, 450)
        InventoryHome.setAutoFillBackground(False)
        InventoryHome.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4,155,180, 255), stop:1 rgba(125,216,87, 255));")
        self.centralwidget = QtWidgets.QWidget(InventoryHome)
        self.centralwidget.setObjectName("centralwidget")
        self.tittle = QtWidgets.QLabel(self.centralwidget)
        self.tittle.setGeometry(QtCore.QRect(40, 10, 161, 31))
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

        self.iProduct = QtWidgets.QLineEdit(self.centralwidget)
        self.iProduct.setGeometry(QtCore.QRect(120, 60, 181, 31))
        self.iProduct.setStyleSheet("background-color: rgb(225, 225, 225);\n"
    "font: 12pt \"Arial\";\n"
    "border-radius: 12px;")
        self.iProduct.setText("")
        self.iProduct.setObjectName("iProduct")
        self.eProduct = QtWidgets.QLabel(self.centralwidget)
        self.eProduct.setGeometry(QtCore.QRect(30, 60, 91, 31))
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
        self.eCant.setGeometry(QtCore.QRect(30, 100, 91, 31))
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
        self.eRef.setGeometry(QtCore.QRect(30, 140, 51, 31))
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
        self.iRef = QtWidgets.QLineEdit(self.centralwidget)
        self.iRef.setGeometry(QtCore.QRect(120, 140, 181, 31))
        self.iRef.setStyleSheet("background-color: rgb(225, 225, 225);\n"
    "font: 12pt \"Arial\";\n"
    "border-radius: 12px;")
        self.iRef.setText("")
        self.iRef.setObjectName("iRef")

        self.eUnit = QtWidgets.QLabel(self.centralwidget)
        self.eUnit.setGeometry(QtCore.QRect(30, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.eUnit.setFont(font)
        self.eUnit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    "color: rgb(255, 255, 255);\n"
    "font: 87 14pt \"Arial\";")
        self.eUnit.setObjectName("eUnit")
        ######## TOTAL LABEL #############
        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(30, 220, 71, 31))
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
        ######## Vr Unit Line Edit #############
        self.iUnit = QtWidgets.QLineEdit(self.centralwidget)
        self.iUnit.setGeometry(QtCore.QRect(120, 180, 181, 31))
        self.iUnit.setStyleSheet("background-color: rgb(225, 225, 225);\n"
    "font: 12pt \"Arial\";\n"
    "border-radius: 12px;")
        self.iUnit.setText("")
        self.iUnit.setObjectName("iUnit")
        self.iUnit.textChanged.connect(self.fVlr)
        ######## Vr Total Line Edit #############
        self.iTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.iTotal.setGeometry(QtCore.QRect(120, 220, 181, 31))
        self.iTotal.setStyleSheet("background-color: rgb(225, 225, 225);\n"
    "font: 12pt \"Arial\";\n"
    "border-radius: 12px;")
        self.iTotal.setText("")
        self.iTotal.setReadOnly(True)
        self.iTotal.setObjectName("iTotal")
        # self.iTotal.textChanged.connect(self.calcTotal)
        ######## Add Selling Button #############
        self.addSell = QtWidgets.QPushButton(self.centralwidget)
        self.addSell.setGeometry(QtCore.QRect(140, 280, 131, 41))
        self.addSell.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addSell.setStyleSheet("background-color: rgb(94, 23, 235);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:15px;\n"
    "font: 87 13pt \"Arial\";")
        self.addSell.setObjectName("addSell")

        self.reportDaily = QtWidgets.QPushButton(self.centralwidget)
        self.reportDaily.setGeometry(QtCore.QRect(390, 90, 121, 41))
        self.reportDaily.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportDaily.setStyleSheet("background-color: rgb(0, 151, 178);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:15px;\n"
    "font: 87 13pt \"Arial\";")
        self.reportDaily.setObjectName("reportDaily")

        self.reportGeneral = QtWidgets.QPushButton(self.centralwidget)
        self.reportGeneral.setGeometry(QtCore.QRect(380, 180, 141, 41))
        self.reportGeneral.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportGeneral.setStyleSheet("background-color: rgb(0, 151, 178);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:15px;\n"
    "font: 87 13pt \"Arial\";")
        self.reportGeneral.setObjectName("reportGeneral")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(520, 370, 61, 41))
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit.setStyleSheet("background-color: rgb(0, 151, 178);\n"
    "color: rgb(255, 255, 255);\n"
    "border-radius:15px;\n"
    "font: 87 13pt \"Arial\";")
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(self.closeWindow)
        ####### SpinBox Cant ##########
        self.spinCant = QtWidgets.QSpinBox(self.centralwidget)
        self.spinCant.setGeometry(QtCore.QRect(120, 100, 181, 31))
        self.spinCant.setStyleSheet("background-color: rgb(225, 225, 225);\n"
    "font: 12pt \"Arial\";\n"
    "border-radius: 12px;")
        self.spinCant.setObjectName("spinCant")
        self.spinCant.valueChanged.connect(self.fCant)
        InventoryHome.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InventoryHome)
        self.statusbar.setObjectName("statusbar")
        InventoryHome.setStatusBar(self.statusbar)

        self.retranslateUi(InventoryHome)
        QtCore.QMetaObject.connectSlotsByName(InventoryHome)

        InventoryHome.show()
        sys.exit(app.exec_())

    def retranslateUi(self, InventoryHome):
        _translate = QtCore.QCoreApplication.translate
        InventoryHome.setWindowTitle(_translate("InventoryHome", "Registro de ventas"))
        self.tittle.setText(_translate("InventoryHome", "Registro de ventas"))
        self.eProduct.setText(_translate("InventoryHome", "Producto:"))
        self.eCant.setText(_translate("InventoryHome", "Cantidad:"))
        self.eRef.setText(_translate("InventoryHome", "Ref.:"))
        self.eUnit.setText(_translate("InventoryHome", "Vr. Unit.:"))
        self.eTotal.setText(_translate("InventoryHome", "Vr. Total:"))
        self.addSell.setText(_translate("InventoryHome", "Agregar Venta"))
        self.reportDaily.setText(_translate("InventoryHome", "Informe Diario"))
        self.reportGeneral.setText(_translate("InventoryHome", "Informe General"))
        self.btnExit.setText(_translate("InventoryHome", "Salir"))

    def calcTotal(self):
        # self.spinCant.value()
        #Aqui la data se está mezclando con el spinbox. I need that data be keeping in memory with before value.
        # print(self.iUnit.text())
        if self.cant != "" and self.vlr != "":
            if int(self.cant) > 0 and int(self.vlr) > 0: 
                total = int(self.cant) * int(self.vlr)
                self.iTotal.setText(str(total))
        elif (self.cant != "" a self.vlr != ""):
            self.iTotal.setText("")

    def fCant(self, data):
        self.cant = data
        self.calcTotal()
    
    def fVlr(self, data):
        self.vlr = data
        self.calcTotal()
    
    def closeWindow(self):
	    exit()


def pandora():
    ref=[4503025, 4514010, 4514006]

    producto = pd.Series(["Arandela 1/4 ZN", "Arandela M10 ZN", "Arandela M6 ZN"],
                     index=ref)
    
    cantidad = pd.Series([3,2,5],
                         index=ref)
    datos = {
	#"Ref": [4503025, 4514010, 4514006, 3],
	"Product": producto,#["arandela", "tornillo", "tuerca"],
    "Cant": cantidad
    }

    datos = pd.DataFrame(datos)
    
    os.makedirs('ProjectInventory/dataBase/', exist_ok=True)
    datos.to_csv('ProjectInventory/DataBase/data.csv', index_label="Ref")
    #datos.to_latex('ProjectInventory/DataBase/data.tex')

def read_data():
     if os.path.isfile('ProjectInventory/DataBase/data.csv'):
        datos = pd.read_csv('ProjectInventory/DataBase/data.csv', index_col="Ref")
        print(datos)
