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
except MySQLdb.Error, e:
    print ("Error connecting to database, %s" % e)
    sys.exit(1)

cursor = connection.cursor()

# request data
pid = int(raw_input("Product ID: "))

# query
try:
    cursor.execute("SELECT * FROM products WHERE prod_id = %d" % (pid))

    row = cursor.fetchone()

    if row is None:
        print ("No item found with ID: %d" % pid)
    else:
        print("ID: %d, Name: %s, Quantity: %d, Price: %f" %
              (row[0], row[1], row[2], row[3]))

        pname = raw_input("New name: ")
        quantity = int(raw_input("New quantity: "))
        price = float(raw_input("New price: "))

        try:
            cursor.execute("""UPDATE products
                              SET prod_name = '%s', quantity = %d, price = %f
                              WHERE prod_id = %d
                            """
                           % (pname, quantity, price, pid))
        except MySQLdb.Error, e:
            print ("Error updating query, %s" % e)
            sys.exit(1)
except MySQLdb.Error, e:
    print ("Error in fetch query, %s" % e)
    sys.exit(1)

# close connection
cursor.close()
connection.commit()
connection.close()
