import os
from datetime import date, timedelta
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from alertBox import AlertBox
from communicator import Communicator
# from Header import Inventory

class Ui_AddProducts(QtWidgets.QDialog):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        self.communicator = Communicator()
        AddProducts = self

        self.datos = []
        self.ref = []
        self.products = []
        self.precios = []
        self.stock = []
        self.cant = ""
        self.vlrUnit = 0
        self.productRef = ""
        self.checkBoxProd = False

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
        self.iProductInv.setGeometry(QtCore.QRect(300, 170, 181, 31))
        self.iProductInv.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iProductInv.setText("")
        self.iProductInv.setObjectName("iProductInv")
        self.eProductInv = QtWidgets.QLabel(self.centralwidget)
        self.eProductInv.setGeometry(QtCore.QRect(150, 170, 121, 31))
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
        self.eCantInv.setGeometry(QtCore.QRect(150, 250, 121, 31))
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
        self.eRefInv.setGeometry(QtCore.QRect(150, 210, 131, 31))
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
        self.addProd.setGeometry(QtCore.QRect(270, 340, 231, 41))
        self.addProd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addProd.setStyleSheet("background-color: rgb(220, 110, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.addProd.setObjectName("addProd")
        self.addProd.clicked.connect(self.fAddInv)

        self.btnBackInv = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackInv.setGeometry(QtCore.QRect(350, 390, 91, 41))
        self.btnBackInv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackInv.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnBackInv.setObjectName("btnBackInv")
        self.btnBackInv.clicked.connect(self.returnMain)

        self.spinCant = QtWidgets.QSpinBox(self.centralwidget)
        self.spinCant.setGeometry(QtCore.QRect(300, 250, 181, 31))
        self.spinCant.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.spinCant.setObjectName("spinCant")
        self.spinCant.setRange(0, 101)
        self.spinCant.valueChanged.connect(self.fCant)

        self.tittle_2 = QtWidgets.QLabel(self.centralwidget)
        self.tittle_2.setGeometry(QtCore.QRect(210, 60, 281, 41))
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

        self.iRefInvS = QtWidgets.QComboBox(self.centralwidget)
        self.iRefInvS.setGeometry(QtCore.QRect(300, 210, 181, 31))
        self.iRefInvS.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iRefInvS.setObjectName("iRefInv")

        self.iRefInvL = QtWidgets.QLineEdit(self.centralwidget)
        self.iRefInvL.setGeometry(QtCore.QRect(300, 210, 181, 31))
        self.iRefInvL.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iRefInvL.setText("")
        self.iRefInvL.setObjectName("iRefInvL")

        self.prodExists = QtWidgets.QCheckBox(self.centralwidget)
        self.prodExists.setGeometry(QtCore.QRect(150, 130, 241, 21))
        self.prodExists.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Tw Cen MT Condensed Extra Bold\";")
        self.prodExists.setObjectName("prodExists")
        self.prodExists.stateChanged.connect(self.toggle_iRef)

        ######## Vr Unit Line Edit #############
        self.iUnit = QtWidgets.QLineEdit(self.centralwidget)
        self.iUnit.setGeometry(QtCore.QRect(300, 290, 181, 31))
        self.iUnit.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iUnit.setText("")
        self.iUnit.setObjectName("iUnit")
        self.iUnit.textChanged.connect(self.fVlr)

        self.eCantInv_2 = QtWidgets.QLabel(self.centralwidget)
        self.eCantInv_2.setGeometry(QtCore.QRect(150, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eCantInv_2.setFont(font)
        self.eCantInv_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eCantInv_2.setObjectName("eCantInv_2")

        self.iRefInvS.setVisible(False)
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
        self.prodExists.setText(_translate("AddProducts", "El producto ya existe?"))
        self.eCantInv_2.setText(_translate("AddProducts", "Precio:"))
    
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

            self.iRefInvS.addItems(self.ref)
    
    def updateProduct(self, data):
        # print(self.ref[data])
        # print(self.products.loc[self.ref[data]])
        self.productRef = self.ref[data]
        if self.checkBoxProd :
            self.iProductInv.setText(self.products.loc[self.productRef])
            self.iUnit.setText(str(self.precios.loc[self.productRef]))

    def toggle_iRef(self, state):
        if state == 2:  # Si el checkbox está marcado
            self.checkBoxProd = True
            self.iRefInvL.setVisible(False)
            self.iRefInvS.setVisible(True)
        else:
            self.checkBoxProd = False
            self.iRefInvL.setVisible(True)
            self.iRefInvS.setVisible(False)
            self.iProductInv.setText("")
            self.iUnit.setText("")

    def fAddInv(self):
        # print(self.products)
        # print(self.iRefInv.text())
        # aviso = ""
        if self.cant != "" and self.cant > 0:
            # print(self.productRef)
            # print(self.iRefInvL.text())
            if self.checkBoxProd:
                sales = pd.Series(self.datos.loc[:,'Ventas'].to_list(), index=self.ref)
                salesToday = pd.Series(self.datos.loc[:,'Sales'].to_list(), index=self.ref)
                datePrev = pd.Series(self.datos.loc[:,'Date'].to_list(), index=self.ref)

                self.datos.loc[self.productRef] = [self.iProductInv.text(), self.vlrUnit, int(self.stock[self.productRef]) + int(self.cant), sales[self.productRef], salesToday[self.productRef], datePrev[self.productRef]]
            else:
                self.datos.loc[self.iRefInvL.text()] = [self.iProductInv.text(), self.vlrUnit, self.cant, 0, salesToday[self.productRef], date.today()-timedelta(days=7)]
            print(self.datos)
        
            os.makedirs('DataBase/', exist_ok=True)
            self.datos.to_csv('DataBase/data.csv', index_label="Ref")
            aviso = "Agregado al inventario\n correctamente"
            # print("TXT AddI YES: " + aviso)
            self.alertBoxW(aviso)
        else:
            aviso = "Cantidad no\npermitida"
            # print("TXT AddI NOT: " + aviso)
            self.alertBoxW(aviso)
        
    
    def alertBoxW(self, txt):
        # print("TXT fAB: " + txt)
        if self.alertBoxWindow is None:
            # If window not exists, la crea y pasa como parametro communicator
            self.alertBoxWindow = AlertBox(self.communicator)
        # If already exists, update the text through the communicator with the updateAlertBox
        self.communicator.updateAlertBox.emit(txt)
        self.alertBoxWindow.show()

    def returnMain(self):
        self.hide()
        # Inventory.cargar()
        if self.main_window:
            self.main_window.show()
