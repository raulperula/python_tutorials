#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from example12 import *


class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mdiArea.addSubWindow(self.ui.subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_2)

        QtCore.QObject.connect(self.ui.pushButton_next,
                               QtCore.SIGNAL('clicked()'),
                               self.display_next)
        QtCore.QObject.connect(self.ui.pushButton__back,
                               QtCore.SIGNAL('clicked()'),
                               self.display_back)
        QtCore.QObject.connect(self.ui.pushButton__close,
                               QtCore.SIGNAL('clicked()'),
                               self.close_all)
        QtCore.QObject.connect(self.ui.pushButton_cascade,
                               QtCore.SIGNAL('clicked()'),
                               self.cascade_view)
        QtCore.QObject.connect(self.ui.pushButton_tail,
                               QtCore.SIGNAL('clicked()'),
                               self.tail_view)
        QtCore.QObject.connect(self.ui.pushButton_subwindow,
                               QtCore.SIGNAL('clicked()'),
                               self.subwindow_view)
        QtCore.QObject.connect(self.ui.pushButton_tab,
                               QtCore.SIGNAL('clicked()'),
                               self.tab_view)

        # menu entries (not necessary in my version)
#         self.connect(self.ui.actionFirst_Window,
#                      QtCore.SIGNAL('triggered()'),
#                      self.display_next)
#         self.connect(self.ui.actionSecond_Window,
#                      QtCore.SIGNAL('triggered()'),
#                      self.display_back)

    def display_next(self):
        """
        User SLOT
        """

        self.ui.mdiArea.activateNextSubWindow()

    def display_back(self):
        """
        User SLOT
        """

        self.ui.mdiArea.activatePreviousSubWindow()

    def close_all(self):
        """
        User SLOT
        """

        self.ui.mdiArea.closeAllSubWindows()

    def cascade_view(self):
        """
        User SLOT
        """

        self.ui.mdiArea.cascadeSubWindows()

    def tail_view(self):
        """
        Mosaic
        """

        self.ui.mdiArea.tileSubWindows()

    def subwindow_view(self):
        """
        User SLOT
        """

        self.ui.mdiArea.setViewMode(0)

    def tab_view(self):
        """
        User SLOT
        """

        self.ui.mdiArea.setViewMode(1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())
