import os
from datetime import date, datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReportGeneral(QtWidgets.QDialog):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        ReportGeneral = self

        self.today = date.today()
        self.datos = []
        self.ref = []
        self.products = []
        self.precios = []
        self.stock = []
        self.dateSell = []
        self.productRef = ""

        ReportGeneral.setObjectName("ReportGeneral")
        ReportGeneral.resize(659, 463)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONOI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReportGeneral.setWindowIcon(icon)
        ReportGeneral.setAutoFillBackground(False)
        ReportGeneral.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4,155,180, 255), stop:1 rgba(125,216,87, 255));")
        self.centralwidget = QtWidgets.QWidget(ReportGeneral)
        self.centralwidget.setObjectName("centralwidget")
        self.tittleGe = QtWidgets.QLabel(self.centralwidget)
        self.tittleGe.setGeometry(QtCore.QRect(60, 30, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittleGe.setFont(font)
        self.tittleGe.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"")
        self.tittleGe.setObjectName("tittleGe")
        self.btnBackGe = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackGe.setGeometry(QtCore.QRect(20, 390, 91, 41))
        self.btnBackGe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackGe.setStyleSheet("background-color: rgb(50, 185, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnBackGe.setObjectName("btnBackGe")
        self.btnBackGe.clicked.connect(self.returnMain)

        self.listProd = QtWidgets.QListWidget(self.centralwidget)
        self.listProd.setGeometry(QtCore.QRect(180, 110, 181, 261))
        self.listProd.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(125,216,87, 255), stop:1 rgba(4,155,180, 255));")
        self.listProd.setObjectName("listProd")
        self.listRef = QtWidgets.QListWidget(self.centralwidget)
        self.listRef.setGeometry(QtCore.QRect(50, 110, 131, 261))
        self.listRef.setStyleSheet("")
        self.listRef.setObjectName("listRef")
        self.listVlr = QtWidgets.QListWidget(self.centralwidget)
        self.listVlr.setGeometry(QtCore.QRect(360, 110, 81, 261))
        self.listVlr.setStyleSheet("")
        self.listVlr.setObjectName("listVlr")
        self.listCant = QtWidgets.QListWidget(self.centralwidget)
        self.listCant.setGeometry(QtCore.QRect(440, 110, 51, 261))
        self.listCant.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(125,216,87, 255), stop:1 rgba(4,155,180, 255));")
        self.listCant.setObjectName("listCant")
        self.listSales = QtWidgets.QListWidget(self.centralwidget)
        self.listSales.setGeometry(QtCore.QRect(490, 110, 51, 261))
        self.listSales.setStyleSheet("")
        self.listSales.setObjectName("listSales")
        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(210, 400, 161, 31))
        self.eTotal.setStyleSheet("")
        self.eTotal.setObjectName("eTotal")
        
        self.retranslateUi(ReportGeneral)
        self.cargar()

    def retranslateUi(self, ReportGeneral):
        _translate = QtCore.QCoreApplication.translate
        ReportGeneral.setWindowTitle(_translate("ReportGeneral", "Informe General de Ventas"))
        self.tittleGe.setText(_translate("ReportGeneral", "INFORME GENERAL DE VENTAS"))
        self.btnBackGe.setText(_translate("ReportGeneral", "Atrás"))
        self.eTotal.setText(_translate("ReportGeneral", "Total Ventas:"))

    def cargar(self):
        if os.path.isfile('DataBase/data.csv'):
            self.datos = pd.read_csv('DataBase/data.csv', index_col="Ref")
            # print(self.datos)
            self.ref = self.datos.index.to_list()
            self.products = self.datos.loc[:,'Product'].to_list()
            self.precios = self.datos.loc[:,'Valor'].to_list()
            self.stock = self.datos.loc[:,'Cant'].to_list()
            self.sales = self.datos.loc[:,'Ventas'].to_list()
            self.sales = [int(s) for s in self.sales]
            self.dateSell = self.datos.loc[:,'Date'].to_list()
            self.dateSell = [datetime.strptime(d, '%Y-%m-%d').date() for d in self.dateSell]
            # print(self.products)
            
            self.listRef.clear()
            self.listCant.clear()
            self.listProd.clear()
            self.listSales.clear()
            self.listVlr.clear()
            
            for e in range(len(self.ref)):
                # print("PROD: ",self.products[date.today()].iloc[e])
                # print("REF: ",self.ref[date.today()].iloc[e])
                # print("CANT: ",self.stock[date.today()].iloc[e])

                self.listRef.addItem(str(self.ref[e]))
                self.listProd.addItem(str(self.products[e]))
                self.listCant.addItem(str(self.stock[e]))
                self.listSales.addItem(str(self.sales[e]))
                self.listVlr.addItem(str(self.precios[e]))
            self.eTotal.setText("Total ventas: "+str(sum(self.sales)))
        
    def returnMain(self):
        self.close()
        if self.main_window:
            self.main_window.show()
