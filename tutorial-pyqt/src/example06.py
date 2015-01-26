# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example6.ui'
#
# Created: Sun Jan 11 17:51:02 2015
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
        self.pushButtonSum = QtGui.QPushButton(Dialog)
        self.pushButtonSum.setGeometry(QtCore.QRect(140, 190, 98, 27))
        self.pushButtonSum.setObjectName(_fromUtf8("pushButtonSum"))
        self.labelNumber1 = QtGui.QLabel(Dialog)
        self.labelNumber1.setGeometry(QtCore.QRect(15, 50, 111, 20))
        self.labelNumber1.setObjectName(_fromUtf8("labelNumber1"))
        self.labelNumber2 = QtGui.QLabel(Dialog)
        self.labelNumber2.setGeometry(QtCore.QRect(15, 90, 111, 20))
        self.labelNumber2.setObjectName(_fromUtf8("labelNumber2"))
        self.labelResult = QtGui.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(55, 140, 81, 20))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.lineEditNumber1 = QtGui.QLineEdit(Dialog)
        self.lineEditNumber1.setGeometry(QtCore.QRect(140, 50, 113, 27))
        self.lineEditNumber1.setObjectName(_fromUtf8("lineEditNumber1"))
        self.lineEditNumber2 = QtGui.QLineEdit(Dialog)
        self.lineEditNumber2.setGeometry(QtCore.QRect(140, 90, 113, 27))
        self.lineEditNumber2.setObjectName(_fromUtf8("lineEditNumber2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSum.setText(QtGui.QApplication.translate("Dialog", "Sum", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNumber1.setText(QtGui.QApplication.translate("Dialog", "First number", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNumber2.setText(QtGui.QApplication.translate("Dialog", "Second number", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResult.setText(QtGui.QApplication.translate("Dialog", "Result", None, QtGui.QApplication.UnicodeUTF8))

