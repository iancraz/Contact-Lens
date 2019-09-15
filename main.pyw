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
            sag1 = float(self.sag1LineEdit.text())
            sag2 = float(self.sag2LineEdit.text())
            sag3 = float(self.sag3LineEdit.text())
            rad1 = float(self.rad1LineEdit.text())
            rad2 = float(self.rad2LineEdit.text())
            rad3 = float(self.rad3LineEdit.text())
        except ValueError:
            return
        


        dist1 = sqrt(4*rad1**2 - 4*(rad1-sag1)**2)
        dist2 = sqrt(4*rad2**2 - 4*(rad2-sag2)**2)
        dist3 = sqrt(4*rad3**2 - 4*(rad3-sag3)**2)

        
        x = linspace(-dist3/2,dist3/2,num= number)
    
        #h1 = rad1 - 1/2 * sqrt(4 * rad1**2 - dist1**2)
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