#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example21 import *
from PyQt4 import QtSql


def create_connection():
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('tutorial_pyqt')
    db.setUserName('root')
    db.setPassword('260188')

    db.open()

    print (db.lastError().text())

    return True


class MyForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("SELECT * FROM products")

        # default display
        self.rec_num = 0
        self.record = self.model.record(self.rec_num)

        print self.record.value("prod_id").toString()

        self.ui.lineEdit_id.setText(self.record.value("prod_id").toString())
        self.ui.lineEdit_name.setText(
            self.record.value("prod_name").toString())
        self.ui.lineEdit_quantity.setText(
            self.record.value("quantity").toString())
        self.ui.lineEdit_price.setText(self.record.value("price").toString())

        QtCore.QObject.connect(self.ui.pushButton_first,
                               QtCore.SIGNAL('clicked()'),
                               self.display_first)
        QtCore.QObject.connect(self.ui.pushButton_last,
                               QtCore.SIGNAL('clicked()'),
                               self.display_last)
        QtCore.QObject.connect(self.ui.pushButton_previous,
                               QtCore.SIGNAL('clicked()'),
                               self.display_previous)
        QtCore.QObject.connect(self.ui.pushButton_next,
                               QtCore.SIGNAL('clicked()'),
                               self.display_next)

    def display_first(self):
        self.rec_num = 0

        self.record = self.model.record(self.rec_num)

        self.ui.lineEdit_id.setText(self.record.value("prod_id").toString())
        self.ui.lineEdit_name.setText(
            self.record.value("prod_name").toString())
        self.ui.lineEdit_quantity.setText(
            self.record.value("quantity").toString())
        self.ui.lineEdit_price.setText(self.record.value("price").toString())

    def display_last(self):
        self.rec_num = self.model.rowCount() - 1

        self.record = self.model.record(self.rec_num)

        self.ui.lineEdit_id.setText(self.record.value("prod_id").toString())
        self.ui.lineEdit_name.setText(
            self.record.value("prod_name").toString())
        self.ui.lineEdit_quantity.setText(
            self.record.value("quantity").toString())
        self.ui.lineEdit_price.setText(self.record.value("price").toString())

    def display_previous(self):
        self.rec_num -= 1

        # check limit
        if self.rec_num < 0:
            self.rec_num = self.model.rowCount() - 1

        self.record = self.model.record(self.rec_num)

        self.ui.lineEdit_id.setText(self.record.value("prod_id").toString())
        self.ui.lineEdit_name.setText(
            self.record.value("prod_name").toString())
        self.ui.lineEdit_quantity.setText(
            self.record.value("quantity").toString())
        self.ui.lineEdit_price.setText(self.record.value("price").toString())

    def display_next(self):
        self.rec_num += 1

        # check limit
        if self.rec_num > self.model.rowCount() - 1:
            self.rec_num = 0

        self.record = self.model.record(self.rec_num)

        self.ui.lineEdit_id.setText(self.record.value("prod_id").toString())
        self.ui.lineEdit_name.setText(
            self.record.value("prod_name").toString())
        self.ui.lineEdit_quantity.setText(
            self.record.value("quantity").toString())
        self.ui.lineEdit_price.setText(self.record.value("price").toString())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    if not create_connection():
        sys.exit(1)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
