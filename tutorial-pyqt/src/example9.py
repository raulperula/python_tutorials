# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example9.ui'
#
# Created: Sun Jan 11 18:36:25 2015
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
        Dialog.resize(430, 320)
        self.pushButtonCalc = QtGui.QPushButton(Dialog)
        self.pushButtonCalc.setGeometry(QtCore.QRect(100, 260, 98, 27))
        self.pushButtonCalc.setObjectName(_fromUtf8("pushButtonCalc"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButtonSum = QtGui.QRadioButton(Dialog)
        self.radioButtonSum.setGeometry(QtCore.QRect(40, 120, 116, 22))
        self.radioButtonSum.setObjectName(_fromUtf8("radioButtonSum"))
        self.radioButtonSub = QtGui.QRadioButton(Dialog)
        self.radioButtonSub.setGeometry(QtCore.QRect(40, 150, 116, 22))
        self.radioButtonSub.setObjectName(_fromUtf8("radioButtonSub"))
        self.radioButtonMultiply = QtGui.QRadioButton(Dialog)
        self.radioButtonMultiply.setGeometry(QtCore.QRect(40, 180, 116, 22))
        self.radioButtonMultiply.setObjectName(_fromUtf8("radioButtonMultiply"))
        self.radioButtonDivide = QtGui.QRadioButton(Dialog)
        self.radioButtonDivide.setGeometry(QtCore.QRect(40, 210, 116, 22))
        self.radioButtonDivide.setObjectName(_fromUtf8("radioButtonDivide"))
        self.lineEditNumber1 = QtGui.QLineEdit(Dialog)
        self.lineEditNumber1.setGeometry(QtCore.QRect(130, 30, 113, 27))
        self.lineEditNumber1.setObjectName(_fromUtf8("lineEditNumber1"))
        self.lineEditNumber2 = QtGui.QLineEdit(Dialog)
        self.lineEditNumber2.setGeometry(QtCore.QRect(130, 70, 113, 27))
        self.lineEditNumber2.setObjectName(_fromUtf8("lineEditNumber2"))
        self.labelResult = QtGui.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(250, 270, 66, 17))
        self.labelResult.setObjectName(_fromUtf8("labelResult"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCalc.setText(QtGui.QApplication.translate("Dialog", "Calc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Number 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Number 2", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonSum.setText(QtGui.QApplication.translate("Dialog", "Sum", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonSub.setText(QtGui.QApplication.translate("Dialog", "Subtraction", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonMultiply.setText(QtGui.QApplication.translate("Dialog", "Multiply", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDivide.setText(QtGui.QApplication.translate("Dialog", "Divide", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResult.setText(QtGui.QApplication.translate("Dialog", "Total", None, QtGui.QApplication.UnicodeUTF8))

