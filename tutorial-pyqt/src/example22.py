# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example22.ui'
#
# Created: Mon Jan 26 12:33:11 2015
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
        Dialog.resize(431, 313)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 60, 411, 191))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 411, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_filter = QtGui.QPushButton(self.widget)
        self.pushButton_filter.setObjectName(_fromUtf8("pushButton_filter"))
        self.horizontalLayout.addWidget(self.pushButton_filter)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 260, 411, 29))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_update = QtGui.QPushButton(self.widget1)
        self.pushButton_update.setObjectName(_fromUtf8("pushButton_update"))
        self.horizontalLayout_2.addWidget(self.pushButton_update)
        self.pushButton_cancel = QtGui.QPushButton(self.widget1)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.pushButton_add = QtGui.QPushButton(self.widget1)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_delete = QtGui.QPushButton(self.widget1)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.horizontalLayout_2.addWidget(self.pushButton_delete)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Product name", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filter.setText(QtGui.QApplication.translate("Dialog", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_update.setText(QtGui.QApplication.translate("Dialog", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))

