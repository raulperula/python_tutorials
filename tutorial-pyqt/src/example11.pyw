#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example11 import *


class MyForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

#         QtCore.QObject.connect(self.ui.pushButton_calc,
#                                QtCore.SIGNAL('clicked()'),
#                                self.calc)
        QtCore.QObject.connect(self.ui.checkBox_pizza20,
                               QtCore.SIGNAL('clicked()'),
                               self.calc)
        QtCore.QObject.connect(self.ui.checkBox_salad5,
                               QtCore.SIGNAL('clicked()'),
                               self.calc)
        QtCore.QObject.connect(self.ui.checkBox_chips10,
                               QtCore.SIGNAL('clicked()'),
                               self.calc)
        QtCore.QObject.connect(self.ui.checkBox_chicken25,
                               QtCore.SIGNAL('clicked()'),
                               self.calc)

    def calc(self):
        """
        User SLOT
        """

        prize = 0
        # set the operation
        if self.ui.checkBox_pizza20.isChecked():
            prize += 20
        if self.ui.checkBox_salad5.isChecked():
            prize += 5
        if self.ui.checkBox_chips10.isChecked():
            prize += 10
        if self.ui.checkBox_chicken25.isChecked():
            prize += 25

        # show the result in the window
        self.ui.lineEdit_total.setText(str(prize))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
