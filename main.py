import sqlite3
import cv2
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot, QTimer
from PyQt4.QtGui import QDialog, QApplication, QImage, QPixmap,QWidget
from  PyQt4.uic import loadUi
import recognation
import data_test
from app2 import  otherwindow
from  other import Ui_Dialog
import trainer
from PIL import Image

import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class app(QDialog) :


    def __init__(self):
        super(app,self).__init__()
        loadUi('app.ui',self)
        self.image=None
        self.recognizer = cv2.createLBPHFaceRecognizer()

        

        self.pushButton.clicked.connect(self.startWebcam)
        self.pushButton1.clicked.connect(self.stopWebcam)

        self.pushButtonAdd.clicked.connect(self.openWindow)
        self.pushButtonUpdate.clicked.connect(lambda: self.classUpdate())
        self.faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
        self.commandLinkButton.clicked.connect(lambda: self.checkAttandence() )


    def openWindow(self):
        self.window1 = QtGui.QDialog()
        self.window1.setWindowTitle('Ajouter Etudiant')
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window1)
        self.window1.hide()
        self.window1.show()




    @pyqtSlot()
    def stopWebcam(self):
        self.timer.stop()
        self.cam.release()
        classe = unicode(self.comboBox.currentText())
        classe = str(classe)
        trainer.setTrainer(classe, classe + '/')
        self.recognizer.load("trainner//" + classe + ".yml")

    def startWebcam(self):
        classe = unicode(self.comboBox.currentText())
        classe = str(classe)
        trainer.setTrainer(classe, classe + '/')
        self.recognizer.load("trainner//" + classe + ".yml")
        self.L=[]
        self.cam = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateF)
        self.timer.start(5)




    def updateF(self):


        font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
        ret, self.image = self.cam.read();
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)



        faces = self.faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 155), 2)
            Id, conf = self.recognizer.predict(gray[y:y + h, x:x + w])

            classe = unicode(self.comboBox.currentText())
            classe = str(classe)
            self.L.append(Id)
            cv2.cv.PutText(cv2.cv.fromarray(self.image), str(data_test.etudiantParID(classe,Id)), (x, y + h), font, 255)
            print self.L

        self.displayImage(self.image,1)

    def  displayImage(self,img,window=1):

        qformat=QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4 :
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        out=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        out=out.rgbSwapped()
        if window==1:

            self.label.setPixmap(QPixmap.fromImage(out))
            self.label.setScaledContents(True)

    def shot(self):
        a = recognation.setPics()
        a.start()

    def Update(self,u):

        conn = sqlite3.connect('tabbb.db')
        c = conn.cursor()


        recs = c.execute("""SELECT * FROM {} ORDER BY nom """.format(u))
        data = c.fetchall()
        i=0

        for row in data:
            item = (str(row[0]) + " " + str(row[1]) )

            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.topLevelItem(i).setText(0, _translate("Dialog", item, None))
            i=i+1
            data_test.dernierID(u)
    def classUpdate(self):

        self.treeWidget.clear()
        classe = unicode(self.comboBox.currentText())
        classe=str(classe)

        self.Update(classe)


    def checkAttandence(self):
        classe = unicode(self.comboBox.currentText())
        classe = str(classe)
        conn = sqlite3.connect('tabbb.db')
        c = conn.cursor()

        recs = c.execute("""SELECT * FROM {} ORDER BY nom""".format(classe))
        conn.commit()
        dattta=c.fetchall()


        ii=0
        for roww in dattta:

            if (roww[2] in self.L) and (self.L.count(roww[2])>6):
                item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
                self.treeWidget.topLevelItem(ii).setText(1, _translate("Dialog", "present", None))
            else:
                item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
                self.treeWidget.topLevelItem(ii).setText(1, _translate("Dialog", "absent", None))

            ii=ii+1

        self.L=[]













ap= QApplication(sys.argv)
window=app()
window.setWindowTitle('Check Presence')
window.show()
sys.exit(ap.exec_())
