import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS movie;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS movie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        year INTEGER,
        score REAL
    )
""")

cur.execute("""
    INSERT INTO movie (title, year, score) VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

cur.executemany("INSERT INTO movie (title, year, score) VALUES (?, ?, ?)",
                data)
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)


def atualizar_movie(year, title, id):
    data = (year, title, id)
    cur.execute("UPDATE movie SET year=?, title=? WHERE id=?;", data)
    con.commit()


atualizar_movie(2024, 'Nova inserção', 1)


def delete_movie(id):
    try:
        cur.execute("DELETE FROM movie WHERE id=?", (id,))
        con.commit()
    except Exception as e:
        print("Error deleting", e)
    
    
delete_movie(2)


for row in cur.execute("SELECT year, title FROM movie ORDER BY id"):
    print(row)

con.close()
