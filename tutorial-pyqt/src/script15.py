#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import MySQLdb
import sys

# open connection
connection = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="260188",
                             db="tutorial_pyqt")
cursor = connection.cursor()

# query
try:
    cursor.execute("""
    create table products (prod_id smallint NOT NULL,
    prod_name char(50),
    quantity smallint,
    price float)
    """)
except MySQLdb.Error:
    print ("Error creating table <products>")
    sys.exit()

# close connection
cursor.close()
connection.close()
