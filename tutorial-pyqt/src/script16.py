#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import MySQLdb
import sys

# open connection
try:
    connection = MySQLdb.connect(host="localhost",
                                 user="root",
                                 passwd="260188",
                                 db="tutorial_pyqt")
except MySQLdb.Error:
    print ("Error connecting to database")
    sys.exit(1)

cursor = connection.cursor()

inserting = "YES"

while inserting.upper() == "YES":
    # request data
    pid = int(raw_input("Product ID: "))
    pname = raw_input("Product name: ")
    quantity = int(raw_input("Quantity: "))
    price = float(raw_input("Price: "))

    # query
    try:
        cursor.execute("""
        INSERT INTO products (prod_id, prod_name, quantity, price)
        VALUES (%d, '%s', %d, %f)
        """ % (pid, pname, quantity, price))

        connection.commit()

        inserting = raw_input("More products? (yes, no): ")
    except MySQLdb.Error, e:
        print ("Error inserting tuple in table <products>, %s" % e)
        connection.rollback()
        sys.exit(1)

# close connection
cursor.close()
connection.close()
