#!/usr/bin/env python3

"""
Program:Database search 
File:db_search.py
Version:1.0
Date:May-6-2019
Author: Yobi Livingstone, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Database Seacrh 
--------------------------------------------------------------------------
Usage: Connection to the SQL database to perform search
--------------------------------------------------------------------------
Import libraries: import pymysql.cursors
"""
import pymysql.cursors

from SQL_python_functions import sql_query as sq

# Set parameters
dbname   = "ly001"
dbhost   = "hope" #If you have an issue, switch ssh to hope
dbuser   = "ly001"   # Ask a demonstrator
dbpass   = "7#b8tpkum"   # Ask a demonstrator
port     = 3306

accession_no=''

# Create SQL statement to find number of human protein entries
sq.db_summary(accession_no)

# Connect to the database
db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

# Create a cursor and execute the SQL on it
cursor = db.cursor()
nrows  = cursor.execute(sql)

# We know there is only one row returned to fetch it and print the data
a = cursor.fetchall()
