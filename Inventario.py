# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inventario.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportDaily(object):
    def setupUi(self, ReportDaily):
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
        self.tittleDi.setGeometry(QtCore.QRect(110, 30, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.tittleDi.setFont(font)
        self.tittleDi.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";\n"
"")
        self.tittleDi.setObjectName("tittleDi")
        self.btnBackDi = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackDi.setGeometry(QtCore.QRect(20, 390, 91, 41))
        self.btnBackDi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBackDi.setStyleSheet("background-color: rgb(50, 185, 41);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnBackDi.setObjectName("btnBackDi")
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(510, 390, 131, 41))
        self.btnNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNext.setStyleSheet("background-color: rgb(249, 167, 25);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 87 14pt \"Arial Black\";")
        self.btnNext.setObjectName("btnNext")
        self.listRef = QtWidgets.QListWidget(self.centralwidget)
        self.listRef.setGeometry(QtCore.QRect(120, 110, 131, 261))
        self.listRef.setStyleSheet("")
        self.listRef.setObjectName("listRef")
        self.listProd = QtWidgets.QListWidget(self.centralwidget)
        self.listProd.setGeometry(QtCore.QRect(250, 110, 181, 261))
        self.listProd.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(125,216,87, 255), stop:1 rgba(4,155,180, 255));")
        self.listProd.setObjectName("listProd")
        self.listCant = QtWidgets.QListWidget(self.centralwidget)
        self.listCant.setGeometry(QtCore.QRect(430, 110, 61, 261))
        self.listCant.setStyleSheet("")
        self.listCant.setObjectName("listCant")
        self.eTotal = QtWidgets.QLabel(self.centralwidget)
        self.eTotal.setGeometry(QtCore.QRect(200, 390, 161, 31))
        self.eTotal.setStyleSheet("")
        self.eTotal.setObjectName("eTotal")
        ReportDaily.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReportDaily)
        QtCore.QMetaObject.connectSlotsByName(ReportDaily)
        ReportDaily.setTabOrder(self.listRef, self.btnBackDi)
        ReportDaily.setTabOrder(self.btnBackDi, self.btnNext)

    def retranslateUi(self, ReportDaily):
        _translate = QtCore.QCoreApplication.translate
        ReportDaily.setWindowTitle(_translate("ReportDaily", "Informe Diario de Ventas"))
        self.tittleDi.setText(_translate("ReportDaily", "INFORME DIARIO DE VENTAS"))
        self.btnBackDi.setText(_translate("ReportDaily", "Atrás"))
        self.btnNext.setText(_translate("ReportDaily", "Siguiente"))
        self.eTotal.setText(_translate("ReportDaily", "Total Ventas:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportDaily = QtWidgets.QMainWindow()
    ui = Ui_ReportDaily()
    ui.setupUi(ReportDaily)
    ReportDaily.show()
    sys.exit(app.exec_())
