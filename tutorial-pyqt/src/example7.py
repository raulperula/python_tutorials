# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example7.ui'
#
# Created: Sun Jan 11 18:11:56 2015
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
        Dialog.resize(431, 300)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(5, 30, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditItemNumber = QtGui.QLineEdit(Dialog)
        self.lineEditItemNumber.setGeometry(QtCore.QRect(110, 20, 113, 27))
        self.lineEditItemNumber.setObjectName(_fromUtf8("lineEditItemNumber"))
        self.lineEditItemPrize = QtGui.QLineEdit(Dialog)
        self.lineEditItemPrize.setGeometry(QtCore.QRect(310, 20, 113, 27))
        self.lineEditItemPrize.setObjectName(_fromUtf8("lineEditItemPrize"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditDiscount = QtGui.QLineEdit(Dialog)
        self.lineEditDiscount.setGeometry(QtCore.QRect(110, 80, 113, 27))
        self.lineEditDiscount.setObjectName(_fromUtf8("lineEditDiscount"))
        self.labelResult = QtGui.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(100, 220, 311, 17))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))
        self.pushButtonCalc = QtGui.QPushButton(Dialog)
        self.pushButtonCalc.setGeometry(QtCore.QRect(180, 150, 98, 27))
        self.pushButtonCalc.setObjectName(_fromUtf8("pushButtonCalc"))
        self.label.setBuddy(self.lineEditItemNumber)
        self.label_2.setBuddy(self.lineEditItemPrize)
        self.label_3.setBuddy(self.lineEditDiscount)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditItemNumber, self.lineEditItemPrize)
        Dialog.setTabOrder(self.lineEditItemPrize, self.lineEditDiscount)
        Dialog.setTabOrder(self.lineEditDiscount, self.pushButtonCalc)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Item &number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Item &prize", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "&Discount (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResult.setText(QtGui.QApplication.translate("Dialog", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCalc.setText(QtGui.QApplication.translate("Dialog", "Calc quantity", None, QtGui.QApplication.UnicodeUTF8))

