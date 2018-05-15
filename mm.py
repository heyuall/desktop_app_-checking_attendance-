# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created: Thu May 10 01:44:58 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(731, 457)
        Dialog.setStyleSheet(_fromUtf8("m"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton1 = QtGui.QPushButton(Dialog)
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.horizontalLayout.addWidget(self.pushButton1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(100, 0, 100, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton2 = QtGui.QPushButton(Dialog)
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.horizontalLayout_3.addWidget(self.pushButton2)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(0, 137))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setText(_fromUtf8(""))
        self.label.setMargin(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.verticalLayout_4.addWidget(self.commandLinkButton)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Malgun Gothic"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setMargin(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.pushButtonUpdate = QtGui.QPushButton(Dialog)
        self.pushButtonUpdate.setObjectName(_fromUtf8("pushButtonUpdate"))
        self.horizontalLayout_6.addWidget(self.pushButtonUpdate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.pushButtonAdd = QtGui.QPushButton(Dialog)
        self.pushButtonAdd.setAutoFillBackground(False)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.verticalLayout_4.addWidget(self.pushButtonAdd)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "stream", None))
        self.pushButton1.setText(_translate("Dialog", "stop", None))
        self.pushButton2.setText(_translate("Dialog", "save", None))
        self.commandLinkButton.setText(_translate("Dialog", "check attendance", None))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "student", None))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "presence", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "Nouvel élément", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "ds", None))
        self.treeWidget.topLevelItem(1).setText(1, _translate("Dialog", "qd", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Dialog", "fgfg", None))
        self.treeWidget.topLevelItem(2).setText(1, _translate("Dialog", "qqqq", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "  Class :", None))
        self.comboBox.setItemText(0, _translate("Dialog", "IA1_1", None))
        self.comboBox.setItemText(1, _translate("Dialog", "IA1_2", None))
        self.comboBox.setItemText(2, _translate("Dialog", "IA2_1", None))
        self.pushButtonUpdate.setText(_translate("Dialog", "Update", None))
        self.pushButtonAdd.setText(_translate("Dialog", "Add / Delete student", None))

