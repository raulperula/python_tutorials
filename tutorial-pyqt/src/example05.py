# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example5.ui'
#
# Created: Sun Jan 11 17:43:28 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.labelWriteName = QtGui.QLabel(Dialog)
        self.labelWriteName.setGeometry(QtCore.QRect(15, 100, 111, 20))
        self.labelWriteName.setObjectName(_fromUtf8("labelWriteName"))
        self.labelMessage = QtGui.QLabel(Dialog)
        self.labelMessage.setGeometry(QtCore.QRect(100, 150, 66, 17))
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.pushButtonPush = QtGui.QPushButton(Dialog)
        self.pushButtonPush.setGeometry(QtCore.QRect(160, 190, 98, 27))
        self.pushButtonPush.setObjectName(_fromUtf8("pushButtonPush"))
        self.lineEditUserName = QtGui.QLineEdit(Dialog)
        self.lineEditUserName.setGeometry(QtCore.QRect(150, 100, 113, 27))
        self.lineEditUserName.setObjectName(_fromUtf8("lineEditUserName"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.labelWriteName.setText(QtGui.QApplication.translate("Dialog", "Write your name", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPush.setText(QtGui.QApplication.translate("Dialog", "Push", None, QtGui.QApplication.UnicodeUTF8))

