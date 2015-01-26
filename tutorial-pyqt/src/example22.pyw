#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example22 import *
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

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("products")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.ui.tableView.setModel(self.model)

        QtCore.QObject.connect(self.ui.pushButton_update,
                               QtCore.SIGNAL('clicked()'),
                               self.update)
        QtCore.QObject.connect(self.ui.pushButton_cancel,
                               QtCore.SIGNAL('clicked()'),
                               self.cancel)
        QtCore.QObject.connect(self.ui.pushButton_add,
                               QtCore.SIGNAL('clicked()'),
                               self.add)
        QtCore.QObject.connect(self.ui.pushButton_delete,
                               QtCore.SIGNAL('clicked()'),
                               self.delete)
        QtCore.QObject.connect(self.ui.pushButton_filter,
                               QtCore.SIGNAL('clicked()'),
                               self.filter)

    def update(self):
        self.model.submitAll()

    def cancel(self):
        self.model.revertAll()

    def add(self):
        self.model.insertRow(
            self.ui.tableView.currentIndex().row())

    def delete(self):
        self.model.removeRow(
            self.ui.tableView.currentIndex().row())
        self.model.submitAll()

    def filter(self):
        self.model.setFilter(
            "prod_name LIKE '" + self.ui.lineEdit.text() + "%'")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    if not create_connection():
        sys.exit(1)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
