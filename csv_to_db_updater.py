# import sqlite3
# import os
# import os.path
# import ctypes

# databaseFile = '.\\testdb.db'
# sqlFile = '.\\sql_ingest.sql'

# # Delete the old table
# if os.path.isfile(databaseFile):
#     os.remove(databaseFile)

# # Create the tables
# qry = open(sqlFile, 'r').read()
# sqlite3.complete_statement(qry)
# conn = sqlite3.connect(databaseFile)
# cursor = conn.cursor()
# try:
#     cursor.executescript(qry)
# except Exception as e:
#     MessageBoxW = ctypes.windll.user32.MessageBoxW
#     errorMessage = databaseFile + ': ' + str(e)
#     MessageBoxW(None, errorMessage, 'Error', 0)
#     cursor.close()
#     raise

import sqlite3, csv

# con = sqlite3.connect(":memory:")
con = sqlite3.connect("test_db.db")
cur = con.cursor()
# cur.executescript("DROP TABLE IF EXISTS meter;CREATE TABLE meter ( SiteID STR, tstamp DATETIME, Reading FLOAT, Unit STR)") 

with open('Test.csv','r') as test_table:
    dr = csv.DictReader(test_table,  ["SiteID", "tstamp", "Reading", "Unit"]) # comma is default delimiter
    to_db = [(i['SiteID'], i['tstamp'], i['Reading'], i['Unit']) for i in dr]

cur.executemany("UPDATE meter SET ('?,?,?,?'), to_db)
con.commit()