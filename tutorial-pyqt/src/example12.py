# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example12.ui'
#
# Created: Sun Jan 18 18:25:33 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(534, 613)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(20, 20, 441, 421))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.subwindow = QtGui.QWidget()
        self.subwindow.setObjectName(_fromUtf8("subwindow"))
        self.label = QtGui.QLabel(self.subwindow)
        self.label.setGeometry(QtCore.QRect(50, 30, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.subwindow_2 = QtGui.QWidget()
        self.subwindow_2.setObjectName(_fromUtf8("subwindow_2"))
        self.label_2 = QtGui.QLabel(self.subwindow_2)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_next = QtGui.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(20, 460, 98, 27))
        self.pushButton_next.setObjectName(_fromUtf8("pushButton_next"))
        self.pushButton__back = QtGui.QPushButton(self.centralwidget)
        self.pushButton__back.setGeometry(QtCore.QRect(190, 460, 98, 27))
        self.pushButton__back.setObjectName(_fromUtf8("pushButton__back"))
        self.pushButton__close = QtGui.QPushButton(self.centralwidget)
        self.pushButton__close.setGeometry(QtCore.QRect(350, 460, 98, 27))
        self.pushButton__close.setObjectName(_fromUtf8("pushButton__close"))
        self.pushButton_cascade = QtGui.QPushButton(self.centralwidget)
        self.pushButton_cascade.setGeometry(QtCore.QRect(20, 500, 98, 27))
        self.pushButton_cascade.setObjectName(_fromUtf8("pushButton_cascade"))
        self.pushButton_tail = QtGui.QPushButton(self.centralwidget)
        self.pushButton_tail.setGeometry(QtCore.QRect(140, 500, 98, 27))
        self.pushButton_tail.setObjectName(_fromUtf8("pushButton_tail"))
        self.pushButton_subwindow = QtGui.QPushButton(self.centralwidget)
        self.pushButton_subwindow.setGeometry(QtCore.QRect(260, 500, 121, 27))
        self.pushButton_subwindow.setObjectName(_fromUtf8("pushButton_subwindow"))
        self.pushButton_tab = QtGui.QPushButton(self.centralwidget)
        self.pushButton_tab.setGeometry(QtCore.QRect(400, 500, 98, 27))
        self.pushButton_tab.setObjectName(_fromUtf8("pushButton_tab"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.subwindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Subwindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.subwindow_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Subwindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton__back.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton__close.setText(QtGui.QApplication.translate("MainWindow", "Close All", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cascade.setText(QtGui.QApplication.translate("MainWindow", "Cascade", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_tail.setText(QtGui.QApplication.translate("MainWindow", "Tail", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_subwindow.setText(QtGui.QApplication.translate("MainWindow", "View Subwindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_tab.setText(QtGui.QApplication.translate("MainWindow", "View Tab", None, QtGui.QApplication.UnicodeUTF8))

