#!/usr/bin/python3
import MySQLdb as sql
import sys

if __name__ == "__main__":
    conn = sql.connect(host="localhost", user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], port=3306)
    col = sys.argv[4]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s", (col,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
