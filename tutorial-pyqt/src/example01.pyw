#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
import atexit
from PyQt4 import QtGui, QtCore


class ExampleWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # set window size (x, y, width, height)
        self.setGeometry(300, 300, 200, 200)
        # set window title
        self.setWindowTitle('Example Window')

        # create push button
        close = QtGui.QPushButton('Close', self)
        close.setGeometry(10, 10, 70, 40)

        # signal-slot connection events
        self.connect(close,
                     QtCore.SIGNAL('clicked()'),
                     QtGui.qApp,
                     QtCore.SLOT('quit()'))

# main
# always needed
app = QtGui.QApplication(sys.argv)
window = ExampleWindow()
# show the window
window.show()
# loop event manager
sys.exit(app.exec_())
