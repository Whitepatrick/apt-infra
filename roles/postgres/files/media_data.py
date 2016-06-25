#/usr/bin/python

import psycopg2

# Try to connect

try:
    conn=psycopg2.connect("dbname='media_data' user='zaphod'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()
try:
    cur.execute("""SELECT * from pg_shadow""")
except:
    print "I can't SELECT from pg_shadow"

rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "   ", row[1]
