import os
import sys
from datetime import date
import pandas as pd
# import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

from alertBox import AlertBox
from Inventario import Ui_ReportDaily
# from ReportGeneral import Ui_ReportGeneral
from InventoryRegis import Ui_AddProducts

os.makedirs('ProjectInventory/DataBase', exist_ok=True)



class Inventory():
    def __init__(self):
        self.datos = []
        self.ref = []
        self.products = []
        self.precios = []
        self.stock = []
        self.cant = ""
        self.vlrUnit = 0
        self.productRef = ""

        app = QtWidgets.QApplication(sys.argv)
        self.InventoryHome = QtWidgets.QMainWindow()
        self.InventoryHome.setObjectName("InventoryHome")
        self.InventoryHome.resize(659, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONOI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InventoryHome.setWindowIcon(icon)
        self.InventoryHome.setAutoFillBackground(False)
        self.InventoryHome.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4,155,180, 255), stop:1 rgba(125,216,87, 255));")
        self.centralwidget = QtWidgets.QWidget(self.InventoryHome)
        self.centralwidget.setObjectName("centralwidget")
        self.tittle = QtWidgets.QLabel(self.centralwidget)
        self.tittle.setGeometry(QtCore.QRect(140, 20, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittle.setFont(font)
        self.tittle.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"\n"
"")
        self.tittle.setObjectName("tittle")

        """ self.eAlerta = QtWidgets.QLabel(self.centralwidget)
        self.eAlerta.setGeometry(QtCore.QRect(280, 60, 71, 31))
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
        self.eAlerta.setObjectName("eAlerta") """

        self.iProduct = QtWidgets.QLineEdit(self.centralwidget)
        self.iProduct.setGeometry(QtCore.QRect(170, 110, 181, 31))
        self.iProduct.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iProduct.setText("")
        self.iProduct.setObjectName("iProduct")
        self.eProduct = QtWidgets.QLabel(self.centralwidget)
        self.eProduct.setGeometry(QtCore.QRect(20, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eProduct.setFont(font)
        self.eProduct.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eProduct.setObjectName("eProduct")

        self.eCant = QtWidgets.QLabel(self.centralwidget)
        self.eCant.setGeometry(QtCore.QRect(20, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eCant.setFont(font)
        self.eCant.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eCant.setObjectName("eCant")
        ####### SpinBox Cant ##########
        self.spinCant = QtWidgets.QSpinBox(self.centralwidget)
        self.spinCant.setGeometry(QtCore.QRect(170, 190, 181, 31))
        self.spinCant.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.spinCant.setObjectName("spinCant")
        self.spinCant.valueChanged.connect(self.fCant)

        self.eRef = QtWidgets.QLabel(self.centralwidget)
        self.eRef.setGeometry(QtCore.QRect(20, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eRef.setFont(font)
        self.eRef.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eRef.setObjectName("eRef")
        self.iRef = QtWidgets.QComboBox(self.centralwidget)
        self.iRef.setGeometry(QtCore.QRect(170, 150, 181, 31))
        self.iRef.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iRef.setObjectName("iRef")
        self.iRef.currentIndexChanged.connect(self.updateProduct)

        self.eUnit = QtWidgets.QLabel(self.centralwidget)
        self.eUnit.setGeometry(QtCore.QRect(20, 230, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eUnit.setFont(font)
        self.eUnit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eUnit.setObjectName("eUnit")
        ######## TOTAL LABEL #############
        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(20, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eTotal.setFont(font)
        self.eTotal.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Bahnschrift SemiBold\";\n"
"font: 18pt \"Tw Cen MT Condensed Extra Bold\";")
        self.eTotal.setObjectName("eTotal")
        ######## Vr Unit Line Edit #############
        self.iUnit = QtWidgets.QLineEdit(self.centralwidget)
        self.iUnit.setGeometry(QtCore.QRect(170, 230, 181, 31))
        self.iUnit.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iUnit.setText("")
        self.iUnit.setObjectName("iUnit")
        self.iUnit.textChanged.connect(self.fVlr)
        ######## Vr Total Line Edit #############
        self.iTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.iTotal.setGeometry(QtCore.QRect(170, 270, 181, 31))
        self.iTotal.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 12px;")
        self.iTotal.setText("")
        self.iTotal.setReadOnly(True)
        self.iTotal.setObjectName("iTotal")
        
        ######## Add Selling Button #############
        self.addSell = QtWidgets.QPushButton(self.centralwidget)
        self.addSell.setGeometry(QtCore.QRect(160, 320, 211, 41))
        self.addSell.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addSell.setStyleSheet("background-color: rgb(73, 149, 66);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.addSell.setObjectName("addSell")
        self.addSell.clicked.connect(self.fAddSell)
        ######### Daily Report Button #################
        self.reportDaily = QtWidgets.QPushButton(self.centralwidget)
        self.reportDaily.setGeometry(QtCore.QRect(400, 160, 191, 41))
        self.reportDaily.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportDaily.setStyleSheet("background-color: rgb(58, 152, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.reportDaily.setObjectName("reportDaily")
        self.reportDaily.clicked.connect(self.reportDailyW)
        ######### General Report Button #################
        self.reportGeneral = QtWidgets.QPushButton(self.centralwidget)
        self.reportGeneral.setGeometry(QtCore.QRect(400, 210, 211, 41))
        self.reportGeneral.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportGeneral.setStyleSheet("background-color: rgb(58, 152, 132);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.reportGeneral.setObjectName("reportGeneral")
        # self.reportGeneral.clicked.connect(self.reportGeneralW)
        ############### Add Product Button #############
        self.addProductoVen = QtWidgets.QPushButton(self.centralwidget)
        self.addProductoVen.setGeometry(QtCore.QRect(400, 260, 231, 41))
        self.addProductoVen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addProductoVen.setStyleSheet("background-color: rgb(99, 38, 140);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.addProductoVen.setObjectName("addProductoVen")
        self.addProductoVen.clicked.connect(self.inventoryRegisW)
        ################ Exit Button #################
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(220, 370, 91, 41))
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit.setStyleSheet("background-color: rgb(200, 15, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(self.closeWindow)
        self.eInformes = QtWidgets.QLabel(self.centralwidget)
        self.eInformes.setGeometry(QtCore.QRect(400, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(10)
        self.eInformes.setFont(font)
        self.eInformes.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"text-decoration: underline;")
        self.eInformes.setObjectName("eInformes")
        ###### Update Window with current data save on database 
        self.cargar()
        
        self.InventoryHome.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.InventoryHome)
        self.statusbar.setObjectName("statusbar")
        self.InventoryHome.setStatusBar(self.statusbar)

        self.retranslateUi(self.InventoryHome)
        QtCore.QMetaObject.connectSlotsByName(self.InventoryHome)

        self.alertBoxWindow = None
        self.reportDailyWindow = Ui_ReportDaily(main_window=self.InventoryHome)
        # self.reportGeneralWindow = AlertBox(main_window=self.InventoryHome)
        self.inventoryRegisWindow = Ui_AddProducts(main_window=self.InventoryHome)

        self.InventoryHome.show()
        sys.exit(app.exec_())

    def retranslateUi(self, InventoryHome):
        _translate = QtCore.QCoreApplication.translate
        InventoryHome.setWindowTitle(_translate("InventoryHome", "Registro de Ventas"))
        self.tittle.setText(_translate("InventoryHome", "REGISTRO DE VENTAS"))
        self.eProduct.setText(_translate("InventoryHome", "Producto:"))
        self.eCant.setText(_translate("InventoryHome", "Cantidad:"))
        self.eRef.setText(_translate("InventoryHome", "Referencia:"))
        self.eUnit.setText(_translate("InventoryHome", "Vr. Unitario:"))
        self.eTotal.setText(_translate("InventoryHome", "Vr. Total:"))
        self.addSell.setText(_translate("InventoryHome", "Agregar Venta"))
        self.reportDaily.setText(_translate("InventoryHome", "Informe Diario"))
        self.reportGeneral.setText(_translate("InventoryHome", "Informe General"))
        self.btnExit.setText(_translate("InventoryHome", "Salir"))
        self.eInformes.setText(_translate("InventoryHome", "INFORMES"))
        self.addProductoVen.setText(_translate("InventoryHome", "Agregar Producto"))
        # self.eAlerta.setText(_translate("InventoryHome", "  Alerta"))

    def alertBoxW(self, txt):
        if self.alertBoxWindow is None:
            self.alertBoxWindow = AlertBox(txt)
        self.alertBoxWindow.show()

    def reportDailyW(self):
        self.InventoryHome.hide()
        self.reportDailyWindow.show()

    def reportGeneralW(self):
        self.InventoryHome.hide()
        self.reportGeneralWindow.show()

    def inventoryRegisW(self):
        self.InventoryHome.hide()
        self.inventoryRegisWindow.show()

    def calcTotal(self):
        # self.spinCant.value()
        # print(self.iUnit.text())
        if self.cant != "" and self.vlrUnit != "":
            if int(self.cant) > 0 and int(self.vlrUnit) > 0: 
                total = int(self.cant) * int(self.vlrUnit)
                self.iTotal.setText(str(total))
        elif (self.cant == "" or self.vlrUnit == ""):
            self.iTotal.setText("")

    def fCant(self, data):
        self.cant = data
        self.calcTotal()
    
    def fVlr(self, data):
        self.vlrUnit = data
        self.calcTotal()

    def cargar(self):
        if os.path.isfile('DataBase/data.csv'):
            self.datos = pd.read_csv('DataBase/data.csv', index_col="Ref")
            # print(self.datos)
            self.ref = self.datos.index.to_list()
            self.products = pd.Series(self.datos.loc[:,'Product'].to_list(),index=self.ref)
            self.precios = pd.Series(self.datos.loc[:,'Valor'].to_list(), index=self.ref)
            self.stock = pd.Series(self.datos.loc[:,'Cant'].to_list(), index=self.ref)
            # print(self.precios)

            self.iRef.addItems(self.ref)
    
    def updateProduct(self, data):
        # print(self.ref[data])
        # print(self.products.loc[self.ref[data]])
        self.productRef = self.ref[data]
        self.iProduct.setText(self.products.loc[self.productRef])
        # print(self.products.loc[self.productRef])
        # print(self.precios.loc[self.productRef])
        self.iUnit.setText(str(self.precios.loc[self.productRef]))


    def fAddSell(self):
        # print(self.products)
        # print(self.productRef)
        # print(self.cant)
    
        # cantidad = pd.Series([3,2,5],index=ref)
        # self.datos = pd.DataFrame({"Product": producto, "Cant": cantidad})
        # print(self.stock.loc[self.productRef])
        if self.cant != "" and self.stock.loc[self.productRef] != "":
            if int(self.cant) > int(self.stock.loc[self.productRef]):
                self.alertBoxW("Fuera de stock")
            else:
                self.datos.at[self.productRef, 'Cant'] -= self.cant
                self.datos.at[self.productRef, 'Ventas'] += self.cant
                print(self.datos)
            
                os.makedirs('DataBase/', exist_ok=True)
                self.datos.to_csv('DataBase/data.csv', index_label="Ref")
                self.alertBoxW("Venta registrada correctamente")
        else:
            self.alertBoxW("Espacio vacio")
        # print(self.stock)
    
    def closeWindow(self):
	    exit()


def pruebas():
    ref=[4503025, 4514010, 4514006]

    producto = pd.Series(["Arandela 1/4 ZN", "Arandela M10 ZN", "Arandela M6 ZN"], index=ref)
    
    cantidad = pd.Series([3,2,5], index=ref)
    datos = {
	#"Ref": [4503025, 4514010, 4514006, 3],
	"Product": producto,#["arandela", "tornillo", "tuerca"],
    "Cant": cantidad
    }

    datos = pd.DataFrame(datos)
    
    os.makedirs('DataBase/', exist_ok=True)
    datos.to_csv('DataBase/data.csv', index_label="Ref")
    #datos.to_latex('ProjectInventory/DataBase/data.tex')

def read_data():
     if os.path.isfile('./DataBase/data.csv'):
        datos = pd.read_csv('./DataBase/data.csv', index_col="Ref")
        ref=datos.index
        print(ref[2])
        for a, b in datos.items():
            print("AA:", a)
            print(b.iloc[0])
        print(datos.loc[:,'Product'])
        fecha = date.today()
        print("Fecha:", fecha)
        dNumpy = datos.loc[:,'Product'].to_list()
        print(dNumpy)

