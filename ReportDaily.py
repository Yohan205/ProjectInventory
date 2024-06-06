import os
from datetime import date, datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReportDaily(QtWidgets.QDialog):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        ReportDaily = self

        self.today = date.today()
        self.datos = []
        self.ref = []
        self.products = []
        self.precios = []
        self.stock = []
        self.dateSell = []
        self.productRef = ""

        ReportDaily.setObjectName("ReportDaily")
        ReportDaily.resize(659, 463)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONOI.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReportDaily.setWindowIcon(icon)
        ReportDaily.setAutoFillBackground(False)
        ReportDaily.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(4,155,180, 255), stop:1 rgba(125,216,87, 255));")
        self.centralwidget = QtWidgets.QWidget(ReportDaily)
        self.centralwidget.setObjectName("centralwidget")
        self.tittleDi = QtWidgets.QLabel(self.centralwidget)
        self.tittleDi.setGeometry(QtCore.QRect(80, 30, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittleDi.setFont(font)
        self.tittleDi.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"")
        self.tittleDi.setObjectName("tittleDi")
        self.btnBackDi = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackDi.setGeometry(QtCore.QRect(10, 410, 91, 41))
        self.btnBackDi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackDi.setStyleSheet("background-color: rgb(50, 185, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnBackDi.setObjectName("btnBackDi")
        self.btnBackDi.clicked.connect(self.returnMain)
        
        self.listRef = QtWidgets.QListWidget(self.centralwidget)
        self.listRef.setGeometry(QtCore.QRect(120, 130, 131, 261))
        self.listRef.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listRef.setObjectName("listRef")
        self.listProd = QtWidgets.QListWidget(self.centralwidget)
        self.listProd.setGeometry(QtCore.QRect(250, 130, 181, 261))
        self.listProd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listProd.setObjectName("listProd")
        self.listCant = QtWidgets.QListWidget(self.centralwidget)
        self.listCant.setGeometry(QtCore.QRect(430, 130, 91, 261))
        self.listCant.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listCant.setObjectName("listCant")

        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(330, 410, 191, 31))
        self.eTotal.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.eTotal.setObjectName("eTotal")
        self.iRefGe = QtWidgets.QLabel(self.centralwidget)
        self.iRefGe.setGeometry(QtCore.QRect(120, 100, 131, 31))
        self.iRefGe.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iRefGe.setObjectName("iRefGe")
        self.iVenDi = QtWidgets.QLabel(self.centralwidget)
        self.iVenDi.setGeometry(QtCore.QRect(430, 100, 91, 31))
        self.iVenDi.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iVenDi.setObjectName("iVenDi")
        self.iProdDi = QtWidgets.QLabel(self.centralwidget)
        self.iProdDi.setGeometry(QtCore.QRect(250, 100, 181, 31))
        self.iProdDi.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iProdDi.setObjectName("iProdDi")

        self.cargar()
        self.retranslateUi(ReportDaily)
        # QtCore.QMetaObject.connectSlotsByName(ReportDaily)

    def retranslateUi(self, ReportDaily):
        _translate = QtCore.QCoreApplication.translate
        ReportDaily.setWindowTitle(_translate("ReportDaily", "Informe Diario de Ventas"))
        self.tittleDi.setText(_translate("ReportDaily", "INFORME DIARIO DE VENTAS"))
        self.btnBackDi.setText(_translate("ReportDaily", "Atrás"))
        self.eTotal.setText(_translate("ReportDaily", " Total Ventas:"))
        self.iRefGe.setText(_translate("ReportDaily", " Referencia"))
        self.iVenDi.setText(_translate("ReportDaily", " Ventas"))
        self.iProdDi.setText(_translate("ReportDaily", " Productos"))

    def cargar(self):
        if os.path.isfile('DataBase/data.csv'):
            self.datos = pd.read_csv('DataBase/data.csv', index_col="Ref")
            # print(self.datos)
            self.dateSell = self.datos.loc[:,'Date'].to_list()
            self.dateSell = [datetime.strptime(d, '%Y-%m-%d').date() for d in self.dateSell]
            self.ref = pd.Series(self.datos.index.to_list(), index=self.dateSell)
            self.products = pd.Series(self.datos.loc[:,'Product'].to_list(),index=self.dateSell)
            self.precios = pd.Series(self.datos.loc[:,'Valor'].to_list(), index=self.dateSell)
            self.sales = pd.Series(self.datos.loc[:,'Sales'].to_list(), index=self.dateSell)
            # print(self.products)
            
            self.listRef.clear()
            self.listCant.clear()
            self.listProd.clear()
            isToday = False
            for i in self.dateSell:
                # print(type(i), type(date.today()))
                # print("DATE:",(i))
                if (i == self.today):
                    isToday = True
                    # print("date: ", i)
            if isToday:
                # print(type(self.products[self.today]))
                # print(type(self.products[self.today]) == str)
                if type(self.products[self.today]) != str:
                    for e in range(self.products[self.today].count()):
                        # print("PROD: ",self.products[date.today()].iloc[e])
                        # print("REF: ",self.ref[date.today()].iloc[e])
                        # print("CANT: ",self.stock[date.today()].iloc[e])

                        self.listRef.addItem(str(self.ref[self.today].iloc[e]))
                        self.listProd.addItem(str(self.products[self.today].iloc[e]))
                        self.listCant.addItem(str(self.sales[self.today].iloc[e]))
                else:
                    self.listRef.addItem(str(self.ref[self.today]))
                    self.listProd.addItem(str(self.products[self.today]))
                    self.listCant.addItem(str(self.sales[self.today]))
                self.eTotal.setText("Total ventas: "+str(self.sales[self.today].sum()))
        
    def returnMain(self):
        self.close()
        if self.main_window:
            self.main_window.show()

