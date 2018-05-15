import cv2
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot, QTimer
from PyQt4.QtGui import QDialog, QApplication, QImage, QPixmap
from  PyQt4.uic import loadUi


import sys
class otherwindow(QDialog):
    def __init__(self):
        super(otherwindow,self).__init__()
        loadUi('app1.ui',self)



def affiche():
        ap1 = QApplication(sys.argv)
        window1 = otherwindow()
        window1.setWindowTitle('nizar app')
        window1.show()
        sys.exit(ap1.exec_())

















