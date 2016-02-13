#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example03 import *


class MyForm(QtGui.QDialog):

    """
    Class to show a GUI. Could be a form.
    """

    def __init__(self, parent=None):
        """
        Constructor of the class.
        """

        # inheritance initialization
        QtGui.QWidget.__init__(self, parent)

        # from example3
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    # instance of the GUI
    app = QtGui.QApplication(sys.argv)

    # create object
    my_app = MyForm()
    # show GUI
    my_app.show()

    # correct exit from app
    sys.exit(app.exec_())
