# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 170, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 200, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 230, 47, 13))
        self.label_7.setObjectName("label_7")
        self.rad1LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rad1LineEdit.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.rad1LineEdit.setObjectName("rad1LineEdit")
        self.rad2LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rad2LineEdit.setGeometry(QtCore.QRect(150, 110, 113, 20))
        self.rad2LineEdit.setObjectName("rad2LineEdit")
        self.rad3LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rad3LineEdit.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.rad3LineEdit.setObjectName("rad3LineEdit")
        self.sag1LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sag1LineEdit.setGeometry(QtCore.QRect(150, 170, 113, 20))
        self.sag1LineEdit.setObjectName("sag1LineEdit")
        self.sag2LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sag2LineEdit.setGeometry(QtCore.QRect(150, 200, 113, 20))
        self.sag2LineEdit.setObjectName("sag2LineEdit")
        self.sag3LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sag3LineEdit.setGeometry(QtCore.QRect(150, 230, 113, 20))
        self.sag3LineEdit.setObjectName("sag3LineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 310, 61, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficador de Lentes Diaz"))
        self.label.setText(_translate("MainWindow", "Por favor, ingrese las especificaciones"))
        self.label_2.setText(_translate("MainWindow", "Radio 1:"))
        self.label_3.setText(_translate("MainWindow", "Radio 2:"))
        self.label_4.setText(_translate("MainWindow", "Radio 3:"))
        self.label_5.setText(_translate("MainWindow", "Sagital 1:"))
        self.label_6.setText(_translate("MainWindow", "Sagital 2:"))
        self.label_7.setText(_translate("MainWindow", "Sagital 3:"))
        self.pushButton.setText(_translate("MainWindow", "Graficar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
