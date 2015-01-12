#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example5 import *


class MyForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButtonPush,
                               QtCore.SIGNAL('clicked()'),
                               self.show_message)

    def show_message(self):
        """
        User SLOT
        """
        self.ui.labelMessage.setText('Hola ' + self.ui.lineEditUserName.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
