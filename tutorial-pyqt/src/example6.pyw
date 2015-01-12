#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example6 import *


class MyForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButtonSum,
                               QtCore.SIGNAL('clicked()'),
                               self.show_sum)

    def show_sum(self):
        """
        User SLOT
        """

        # check if number one is written
        if len(self.ui.lineEditNumber1.text()) != 0:
            num1 = int(self.ui.lineEditNumber1.text())
        else:
            num1 = 0

        # check if number two is written
        if len(self.ui.lineEditNumber2.text()) != 0:
            num2 = int(self.ui.lineEditNumber2.text())
        else:
            num2 = 0

        # do the sum
        result = num1 + num2

        # show the result in the window
        self.ui.labelResult.setText('Sum: ' + str(result))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
