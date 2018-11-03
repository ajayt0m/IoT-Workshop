import serial
import MySQLdb
import time
conn=MySQLdb.connect("localhost","root","","py2")
cur=conn.cursor()
cur.execute("insert into status(pinstate)values('1')")
conn.commit()
cur.close()
