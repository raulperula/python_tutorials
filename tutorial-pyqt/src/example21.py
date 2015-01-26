# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example21.ui'
#
# Created: Mon Jan 26 10:48:59 2015
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
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 100, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 130, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 160, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_id = QtGui.QLineEdit(Dialog)
        self.lineEdit_id.setGeometry(QtCore.QRect(180, 60, 120, 27))
        self.lineEdit_id.setObjectName(_fromUtf8("lineEdit_id"))
        self.lineEdit_name = QtGui.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(180, 90, 120, 27))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.lineEdit_quantity = QtGui.QLineEdit(Dialog)
        self.lineEdit_quantity.setGeometry(QtCore.QRect(180, 120, 120, 27))
        self.lineEdit_quantity.setObjectName(_fromUtf8("lineEdit_quantity"))
        self.lineEdit_price = QtGui.QLineEdit(Dialog)
        self.lineEdit_price.setGeometry(QtCore.QRect(180, 150, 120, 27))
        self.lineEdit_price.setObjectName(_fromUtf8("lineEdit_price"))
        self.pushButton_first = QtGui.QPushButton(Dialog)
        self.pushButton_first.setGeometry(QtCore.QRect(80, 200, 98, 27))
        self.pushButton_first.setObjectName(_fromUtf8("pushButton_first"))
        self.pushButton_last = QtGui.QPushButton(Dialog)
        self.pushButton_last.setGeometry(QtCore.QRect(80, 240, 98, 27))
        self.pushButton_last.setObjectName(_fromUtf8("pushButton_last"))
        self.pushButton_previous = QtGui.QPushButton(Dialog)
        self.pushButton_previous.setGeometry(QtCore.QRect(210, 200, 98, 27))
        self.pushButton_previous.setObjectName(_fromUtf8("pushButton_previous"))
        self.pushButton_next = QtGui.QPushButton(Dialog)
        self.pushButton_next.setGeometry(QtCore.QRect(210, 240, 98, 27))
        self.pushButton_next.setObjectName(_fromUtf8("pushButton_next"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Product List", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first.setText(QtGui.QApplication.translate("Dialog", "First", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last.setText(QtGui.QApplication.translate("Dialog", "Last", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_previous.setText(QtGui.QApplication.translate("Dialog", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next.setText(QtGui.QApplication.translate("Dialog", "Next", None, QtGui.QApplication.UnicodeUTF8))

