#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
should take 3 arguments username, passwd and db name
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curr = db.cursor()
    print(type(curr))
    curr.execute("""SELECT * FROM states where name LIKE 'N%' ORDER BY states.id ASC""")
    lst = curr.fetchall()
    for r in lst:
        print(r)
    curr.close()
    db.close()
