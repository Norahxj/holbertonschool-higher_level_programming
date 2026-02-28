#!/usr/bin/python3
"""
Displays states matching a user-provided name (unsafe but case-sensitive).
"""

import sys
import MySQLdb


def main():
    """
    Filters states using string formatting (SQL injection vulnerable).
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE name = BINARY '{}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])

    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
