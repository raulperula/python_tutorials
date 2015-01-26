#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example20 import *
from PyQt4 import QtSql, QtGui


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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    if not create_connection():
        sys.exit(1)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
