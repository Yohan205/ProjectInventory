# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportGeneral.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportGeneral(object):
    def setupUi(self, ReportGeneral):
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
        self.tittleGe.setGeometry(QtCore.QRect(70, 30, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittleGe.setFont(font)
        self.tittleGe.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"")
        self.tittleGe.setObjectName("tittleGe")
        self.btnBackGe = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackGe.setGeometry(QtCore.QRect(10, 400, 91, 41))
        self.btnBackGe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackGe.setStyleSheet("background-color: rgb(50, 185, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnBackGe.setObjectName("btnBackGe")
        self.listProd = QtWidgets.QListWidget(self.centralwidget)
        self.listProd.setGeometry(QtCore.QRect(140, 120, 181, 261))
        self.listProd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listProd.setObjectName("listProd")
        self.listRef = QtWidgets.QListWidget(self.centralwidget)
        self.listRef.setGeometry(QtCore.QRect(10, 120, 131, 261))
        self.listRef.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listRef.setObjectName("listRef")
        self.listVlr = QtWidgets.QListWidget(self.centralwidget)
        self.listVlr.setGeometry(QtCore.QRect(320, 120, 101, 261))
        self.listVlr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listVlr.setObjectName("listVlr")
        self.listCant = QtWidgets.QListWidget(self.centralwidget)
        self.listCant.setGeometry(QtCore.QRect(420, 120, 141, 261))
        self.listCant.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listCant.setObjectName("listCant")
        self.listSales = QtWidgets.QListWidget(self.centralwidget)
        self.listSales.setGeometry(QtCore.QRect(560, 120, 91, 261))
        self.listSales.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listSales.setObjectName("listSales")
        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(460, 400, 191, 31))
        self.eTotal.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.eTotal.setObjectName("eTotal")
        self.iRefGe = QtWidgets.QLabel(self.centralwidget)
        self.iRefGe.setGeometry(QtCore.QRect(10, 90, 131, 31))
        self.iRefGe.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iRefGe.setObjectName("iRefGe")
        self.iProdGe = QtWidgets.QLabel(self.centralwidget)
        self.iProdGe.setGeometry(QtCore.QRect(140, 90, 181, 31))
        self.iProdGe.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iProdGe.setObjectName("iProdGe")
        self.iPrecGe = QtWidgets.QLabel(self.centralwidget)
        self.iPrecGe.setGeometry(QtCore.QRect(320, 90, 101, 31))
        self.iPrecGe.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iPrecGe.setObjectName("iPrecGe")
        self.iExiscGe = QtWidgets.QLabel(self.centralwidget)
        self.iExiscGe.setGeometry(QtCore.QRect(420, 90, 141, 31))
        self.iExiscGe.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iExiscGe.setObjectName("iExiscGe")
        self.iVenGe = QtWidgets.QLabel(self.centralwidget)
        self.iVenGe.setGeometry(QtCore.QRect(560, 90, 91, 31))
        self.iVenGe.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.iVenGe.setObjectName("iVenGe")
        ReportGeneral.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReportGeneral)
        QtCore.QMetaObject.connectSlotsByName(ReportGeneral)
        ReportGeneral.setTabOrder(self.listRef, self.listProd)
        ReportGeneral.setTabOrder(self.listProd, self.listVlr)
        ReportGeneral.setTabOrder(self.listVlr, self.listCant)
        ReportGeneral.setTabOrder(self.listCant, self.listSales)
        ReportGeneral.setTabOrder(self.listSales, self.btnBackGe)

    def retranslateUi(self, ReportGeneral):
        _translate = QtCore.QCoreApplication.translate
        ReportGeneral.setWindowTitle(_translate("ReportGeneral", "Informe General de Ventas"))
        self.tittleGe.setText(_translate("ReportGeneral", "INFORME GENERAL DE VENTAS"))
        self.btnBackGe.setText(_translate("ReportGeneral", "Atrás"))
        self.eTotal.setText(_translate("ReportGeneral", " Total Ventas:"))
        self.iRefGe.setText(_translate("ReportGeneral", " Referencia"))
        self.iProdGe.setText(_translate("ReportGeneral", " Productos"))
        self.iPrecGe.setText(_translate("ReportGeneral", " Precio "))
        self.iExiscGe.setText(_translate("ReportGeneral", " Existencias"))
        self.iVenGe.setText(_translate("ReportGeneral", " Ventas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportGeneral = QtWidgets.QMainWindow()
    ui = Ui_ReportGeneral()
    ui.setupUi(ReportGeneral)
    ReportGeneral.show()
    sys.exit(app.exec_())
