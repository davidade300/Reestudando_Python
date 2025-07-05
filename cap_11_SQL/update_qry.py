import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            "UPDATE agenda SET telefone = '12345-6788' WHERE nome = 'David'"
        )

    conn.commit()
