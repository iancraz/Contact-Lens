from PyQt5 import QtWidgets#QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFileDialog,QMessageBox
from userInterface import Ui_MainWindow
from numpy import sqrt,linspace
import matplotlib.pyplot as plt
import sys

PATH = r'C:\Users\Ian Diaz\Documents\LTspiceXVII\lib\sym'

class Logic(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.lensCalculation)
    
    def lensCalculation(self):
        number = 100
        try:
            dist1 = float(self.diam1LineEdit.text())
            dist2 = float(self.diam2LineEdit.text())
            dist3 = float(self.diam3LineEdit.text())
            rad2 = float(self.rad2LineEdit.text())
            rad3 = float(self.rad3LineEdit.text())
            rad1 = float(self.rad1LineEdit.text())
        except ValueError:
            print("No Value")
        
        if self.calcRad.isChecked():
            sag1 = float(self.sagInput.text())
            rad1 = (dist1**2 - 4 * sag1**2)/(8*sag1)
        self.rad1LineEdit.setText(str(rad1))
        
        if self.dryBut.isChecked():
            rad1 = rad1 * float(self.radialIndexLineEdit.text())
            rad2 = rad2 * float(self.radialIndexLineEdit.text())
            rad3 = rad3 * float(self.radialIndexLineEdit.text())
            dist1 = dist1 * float(self.linealIndexLineEdit.text())
            dist2 = dist2 * float(self.linealIndexLineEdit.text())
            dist3 = dist3 * float(self.linealIndexLineEdit.text())
        else:
            rad1 = rad1 / float(self.radialIndexLineEdit.text())
            rad2 = rad2 / float(self.radialIndexLineEdit.text())
            rad3 = rad3 / float(self.radialIndexLineEdit.text())
            dist1 = dist1 / float(self.linealIndexLineEdit.text())
            dist2 = dist2 / float(self.linealIndexLineEdit.text())
            dist3 = dist3 / float(self.linealIndexLineEdit.text())

        self.rad1ans.setText(str(rad1))
        self.rad2ans.setText(str(rad2))
        self.rad3ans.setText(str(rad3))
        self.diam1Ans.setText(str(dist1))
        self.diam2Ans.setText(str(dist2))
        self.diam3Ans.setText(str(dist3))

        #dist1 = sqrt(4*rad1**2 - 4*(rad1-sag1)**2)
        #dist2 = sqrt(4*rad2**2 - 4*(rad2-sag2)**2)
        #dist3 = sqrt(4*rad3**2 - 4*(rad3-sag3)**2)

        
        x = linspace(-dist3/2,dist3/2,num= number)
    
        h1 = rad1 - 1/2 * sqrt(4 * rad1**2 - dist1**2)
        #h2 = rad2 - 1/2 * sqrt(4 * rad2**2 - dist2**2)
        #h3 = rad3 - 1/2 * sqrt(4 * rad3**2 - dist3**2)
        y = []
        for k in x:
            if k < (-dist2/2)  or k > (dist2/2):
                y0 = 0
                y.append(sqrt(rad3**2 - k**2)+y0)
            elif k < (-dist1/2) or k > (dist1/2):
                y1 = sqrt(rad3**2 - (dist2/2)**2) - sqrt(rad2**2 - (dist2/2)**2) + y0
                y.append(sqrt(rad2**2-k**2)+y1)
            elif k > (-dist1/2) or k < (dist1/2):
                y2 = y1  + sqrt(rad2**2 - (dist1/2)**2) - sqrt(rad1**2 - (dist1/2)**2)
                y.append(sqrt(rad1**2-k**2)+y2)

        yt = y[0]
        for k in range(0,len(x)):
            y[k] = y[k]-yt

        plt.plot(x,y)
        bot, top = plt.ylim()
        izq, der = plt.xlim()
        if top-bot > der-izq:
            temp = top-bot
            plt.xlim(izq,izq+temp)
        else:
            temp = der-izq
            temp2 = (top-bot)/2
            plt.ylim(bot-temp/2 + temp2,bot+temp/2 + temp2)
        plt.grid(which='both')
        plt.title("Lente de perfil")
        plt.xlabel("Milimetros")
        plt.ylabel("Milimetros")
        self.sag1LineEdit.setText(str(h1))
        plt.show()
        
        # rad1
        # rad2
        # rad3
        # dist1
        # dist2
        # dist3
        # sag1 = h1
        # sag2 = h2
        # sag3 = h3
        # plot(x,y)
        # axis([(-dist3/2)-0.5 (dist3/2)+0.5 y(1)-dist3/2-0.5 y(1)+dist3/2+0.5]);
        # grid minor
        # title("Lente de Perfil")

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Logic()
    window.show()
    app.exec_()