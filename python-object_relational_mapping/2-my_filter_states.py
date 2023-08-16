#!/usr/bin/python3
"""filter states by user input"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
            id ASC".format(argv[4]))
    my_list = cursor.fetchall()
    for j in my_list:
        if j[1] == argv[4]:
            print(j)
    cursor.close()
    db.close()
