import os
import sys
from datetime import date
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from alertBox import AlertBox


class Ui_AddProducts(QtWidgets.QDialog):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window

        self.datos = []
        self.ref = []
        self.products = []
        self.precios = []
        self.stock = []
        self.cant = ""
        self.vlrUnit = 0
        self.productRef = ""

        AddProducts = self
        AddProducts.setObjectName("AddProducts")
        AddProducts.resize(659, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONOI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddProducts.setWindowIcon(icon)
        AddProducts.setAutoFillBackground(False)
        AddProducts.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4,155,180, 255), stop:1 rgba(125,216,87, 255));")
        self.centralwidget = QtWidgets.QWidget(AddProducts)
        self.centralwidget.setObjectName("centralwidget")
        self.tittleInv = QtWidgets.QLabel(self.centralwidget)
        self.tittleInv.setGeometry(QtCore.QRect(150, 20, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittleInv.setFont(font)
        self.tittleInv.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"\n"
"")
        self.tittleInv.setObjectName("tittleInv")
        self.tittle_2 = QtWidgets.QLabel(self.centralwidget)
        self.tittle_2.setGeometry(QtCore.QRect(210, 70, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittle_2.setFont(font)
        self.tittle_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"\n"
"")
        self.tittle_2.setObjectName("tittle_2")
        self.iProductInv = QtWidgets.QLineEdit(self.centralwidget)
        self.iProductInv.setGeometry(QtCore.QRect(270, 160, 181, 31))
        self.iProductInv.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iProductInv.setText("")
        self.iProductInv.setObjectName("iProductInv")
        self.eProductInv = QtWidgets.QLabel(self.centralwidget)
        self.eProductInv.setGeometry(QtCore.QRect(120, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eProductInv.setFont(font)
        self.eProductInv.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eProductInv.setObjectName("eProductInv")
        self.eCantInv = QtWidgets.QLabel(self.centralwidget)
        self.eCantInv.setGeometry(QtCore.QRect(120, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eCantInv.setFont(font)
        self.eCantInv.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eCantInv.setObjectName("eCantInv")
        self.eRefInv = QtWidgets.QLabel(self.centralwidget)
        self.eRefInv.setGeometry(QtCore.QRect(120, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eRefInv.setFont(font)
        self.eRefInv.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eRefInv.setObjectName("eRefInv")
        self.addProd = QtWidgets.QPushButton(self.centralwidget)
        self.addProd.setGeometry(QtCore.QRect(240, 300, 231, 41))
        self.addProd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addProd.setStyleSheet("background-color: rgb(220, 110, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.addProd.setObjectName("addProd")
        self.addProd.clicked.connect(self.fAddInv)

        self.btnBackInv = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackInv.setGeometry(QtCore.QRect(310, 350, 91, 41))
        self.btnBackInv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackInv.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnBackInv.setObjectName("btnBackInv")
        self.btnBackInv.clicked.connect(self.returnMain)

        self.spinCant = QtWidgets.QSpinBox(self.centralwidget)
        self.spinCant.setGeometry(QtCore.QRect(270, 240, 181, 31))
        self.spinCant.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.spinCant.setObjectName("spinCant")
        self.spinCant.valueChanged.connect(self.fCant)

        self.iRefInv = QtWidgets.QLineEdit(self.centralwidget)
        self.iRefInv.setGeometry(QtCore.QRect(270, 200, 181, 31))
        self.iRefInv.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iRefInv.setText("")
        self.iRefInv.setObjectName("iRefInv")
        # self.iRefInv.currentIndexChanged.connect(self.updateProduct)

        self.cargar()
        # AddProducts.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(AddProducts)
        # self.statusbar.setObjectName("statusbar")
        # AddProducts.setStatusBar(self.statusbar)

        self.alertBoxWindow = None
        self.retranslateUi(AddProducts)
        # QtCore.QMetaObject.connectSlotsByName(AddProducts)

    def retranslateUi(self, AddProducts):
        _translate = QtCore.QCoreApplication.translate
        AddProducts.setWindowTitle(_translate("AddProducts", "Agregar Productos al Inventario"))
        self.tittleInv.setText(_translate("AddProducts", "AGREGAR PRODUCTOS"))
        self.eProductInv.setText(_translate("AddProducts", "Producto:"))
        self.eCantInv.setText(_translate("AddProducts", "Cantidad:"))
        self.eRefInv.setText(_translate("AddProducts", "Referencia:"))
        self.addProd.setText(_translate("AddProducts", "Agregar Producto"))
        self.btnBackInv.setText(_translate("AddProducts", "Atrás"))
        self.tittle_2.setText(_translate("AddProducts", "AL INVENTARIO"))

    def fCant(self, data):
        self.cant = data
    
    def fVlr(self, data):
        self.vlrUnit = data

    def cargar(self):
        if os.path.isfile('DataBase/data.csv'):
            self.datos = pd.read_csv('DataBase/data.csv', index_col="Ref")
            # print(self.datos)
            self.ref = self.datos.index.to_list()
            self.products = pd.Series(self.datos.loc[:,'Product'].to_list(),index=self.ref)
            self.precios = pd.Series(self.datos.loc[:,'Valor'].to_list(), index=self.ref)
            self.stock = pd.Series(self.datos.loc[:,'Cant'].to_list(), index=self.ref)
            # print(self.precios)

            # self.iRef.addItems(self.ref)
    
    def updateProduct(self, data):
        # print(self.ref[data])
        # print(self.products.loc[self.ref[data]])
        self.productRef = self.ref[data]
        self.iProduct.setText(self.products.loc[self.productRef])
        # print(self.products.loc[self.productRef])
        # print(self.precios.loc[self.productRef])
        self.iUnit.setText(str(self.precios.loc[self.productRef]))

    def fAddInv(self):
        # print(self.products)
        # print(self.iRefInv.text())
        self.aviso = ""
        if self.cant != "" and self.cant > 0:
            self.datos.loc[self.iRefInv.text()] = [self.iProductInv.text(), 0, self.cant, 0]
            print(self.datos)
        
            os.makedirs('DataBase/', exist_ok=True)
            self.datos.to_csv('DataBase/data.csv', index_label="Ref")
            self.aviso = "Agregado al inventario correctamente"
        else:
            self.aviso = "Cantidad no permitida"
        self.alertBoxW(self.aviso)
    
    def alertBoxW(self, txt):
        if self.alertBoxWindow is None:
            self.alertBoxWindow = AlertBox(txt)
        self.alertBoxWindow.show()

    def returnMain(self):
        self.hide()
        if self.main_window:
            self.main_window.show()
