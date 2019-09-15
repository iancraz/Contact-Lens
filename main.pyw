from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFileDialog,QMessageBox
from userInterface import *
import numpy as np
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
        sag1 = float(self.sag1LineEdit.text())
        sag2 = float(self.sag2LineEdit.text())
        sag3 = float(self.sag3LineEdit.text())
        rad1 = float(self.rad1LineEdit.text())
        rad2 = float(self.rad2LineEdit.text())
        rad3 = float(self.rad3LineEdit.text())

        dist1 = np.sqrt(4*rad1**2 - 4*(rad1-sag1)**2)
        dist2 = np.sqrt(4*rad2**2 - 4*(rad2-sag2)**2)
        dist3 = np.sqrt(4*rad3**2 - 4*(rad3-sag3)**2)

        step = dist3 /number
        x = np.linspace(-dist3/2,dist3/2,num= number)
    
        h1 = rad1 - 1/2 * np.sqrt(4 * rad1**2 - dist1**2)
        h2 = rad2 - 1/2 * np.sqrt(4 * rad2**2 - dist2**2)
        h3 = rad3 - 1/2 * np.sqrt(4 * rad3**2 - dist3**2)
        y = []
        for k in x:
            if k < (-dist2/2)  or k > (dist2/2):
                y0 = 0
                y.append(np.sqrt(rad3**2 - k**2)+y0)
            elif k < (-dist1/2) or k > (dist1/2):
                y1 = np.sqrt(rad3**2 - (dist2/2)**2) - np.sqrt(rad2**2 - (dist2/2)**2) + y0
                y.append(np.sqrt(rad2**2-k**2)+y1)
            elif k > (-dist1/2) or k < (dist1/2):
                y2 = y1  + np.sqrt(rad2**2 - (dist1/2)**2) - np.sqrt(rad1**2 - (dist1/2)**2)
                y.append(np.sqrt(rad1**2-k**2)+y2)

        yt = y[0]
        for k in range(0,len(x)):
            y[k] = y[k]-yt

        plt.plot(x,y)
        #plt.xlim(-3,3)
        #plt.ylim(0,5)
        plt.grid(which='both')
        plt.title("Lente de perfil")
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