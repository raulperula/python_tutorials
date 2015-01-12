#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example7 import *


class MyForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButtonCalc,
                               QtCore.SIGNAL('clicked()'),
                               self.calc)

    def calc(self):
        """
        User SLOT
        """

        # check if number one is written
        if len(self.ui.lineEditItemNumber.text()) != 0:
            item_number = int(self.ui.lineEditItemNumber.text())
        else:
            item_number = 0

        # check if number two is written
        if len(self.ui.lineEditItemPrize.text()) != 0:
            item_prize = int(self.ui.lineEditItemPrize.text())
        else:
            item_prize = 0

        # check if number two is written
        if len(self.ui.lineEditDiscount.text()) != 0:
            discount = int(self.ui.lineEditDiscount.text())
        else:
            discount = 0

        # calculate the result
        total_prize = item_number * item_prize
        total_discount = total_prize * discount / 100
        result = total_prize - total_discount

        # show the result in the window
        self.ui.labelResult.setText('Total prize: ' + str(total_prize)
                                    + ', Total discount: ' +
                                    str(total_discount)
                                    + ', Result: ' + str(result))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
