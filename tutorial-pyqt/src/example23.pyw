#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)

label = QLabel()
pixmap = QPixmap(sys.argv[1])
label.setPixmap(pixmap)
label.show()

sys.exit(app.exec_())
