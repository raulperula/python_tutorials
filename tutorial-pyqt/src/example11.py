# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example11.ui'
#
# Created: Sun Jan 18 14:27:42 2015
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
        self.checkBox_pizza20 = QtGui.QCheckBox(Dialog)
        self.checkBox_pizza20.setGeometry(QtCore.QRect(40, 60, 97, 22))
        self.checkBox_pizza20.setObjectName(_fromUtf8("checkBox_pizza20"))
        self.checkBox_salad5 = QtGui.QCheckBox(Dialog)
        self.checkBox_salad5.setGeometry(QtCore.QRect(40, 90, 97, 22))
        self.checkBox_salad5.setObjectName(_fromUtf8("checkBox_salad5"))
        self.checkBox_chips10 = QtGui.QCheckBox(Dialog)
        self.checkBox_chips10.setGeometry(QtCore.QRect(40, 120, 97, 22))
        self.checkBox_chips10.setObjectName(_fromUtf8("checkBox_chips10"))
        self.checkBox_chicken25 = QtGui.QCheckBox(Dialog)
        self.checkBox_chicken25.setGeometry(QtCore.QRect(40, 150, 97, 22))
        self.checkBox_chicken25.setObjectName(_fromUtf8("checkBox_chicken25"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_calc = QtGui.QPushButton(Dialog)
        self.pushButton_calc.setGeometry(QtCore.QRect(110, 190, 98, 27))
        self.pushButton_calc.setObjectName(_fromUtf8("pushButton_calc"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_total = QtGui.QLineEdit(Dialog)
        self.lineEdit_total.setEnabled(False)
        self.lineEdit_total.setGeometry(QtCore.QRect(160, 240, 113, 27))
        self.lineEdit_total.setObjectName(_fromUtf8("lineEdit_total"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_pizza20.setText(QtGui.QApplication.translate("Dialog", "Pizza 20€", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_salad5.setText(QtGui.QApplication.translate("Dialog", "Salad 5€", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_chips10.setText(QtGui.QApplication.translate("Dialog", "Chips 10€", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_chicken25.setText(QtGui.QApplication.translate("Dialog", "Chicken 25€", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Pedido Alimentación", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_calc.setText(QtGui.QApplication.translate("Dialog", "Calc prize", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Total prize", None, QtGui.QApplication.UnicodeUTF8))

