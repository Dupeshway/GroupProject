#!/usr/bin/env python3
import pymysql.cursors

# Set parameters
dbname   = "ly001"
dbhost   = "ssh.cryst.bbk.ac.uk"
dbuser   = "ly001"   # Ask a demonstrator
dbpass   = "7#b8tpkum"   # Ask a demonstrator
port     = 3306

# Create SQL statement to find number of human protein entries
sql      = "select *, from GENE"

# Connect to the database
db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

# Create a cursor and execute the SQL on it
cursor = db.cursor()
nrows  = cursor.execute(sql)

# We know there is only one row returned to fetch it and print the data
data   = cursor.fetchone()
print ("There were ", data[0])
