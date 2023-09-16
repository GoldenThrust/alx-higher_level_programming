#!/usr/bin/env python3
import MySQLdb as sql
import sys

if __name__ == "__main__":
    conn = sql.connect(host="localhost", user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], port=3306)

    col = sys.argv[4]
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (col,))
    rows = cursor.fetchall()
    lists = (row[0] for row in rows)

    print(*lists, sep=", ")
    cursor.close()
    conn.close()
