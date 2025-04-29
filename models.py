import sqlite3

connection = sqlite3.connect('gym.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO trainers (name, email) VALUES (?, ?)", ("Alex", "alex@gym.com"))
cur.execute("INSERT INTO trainers (name, email) VALUES (?, ?)", ("Jamie", "jamie@gym.com"))

cur.execute("INSERT INTO clients (name, trainer_id) VALUES (?, ?)", ("Client A", 1))
cur.execute("INSERT INTO clients (name, trainer_id) VALUES (?, ?)", ("Client B", 1))

cur.execute("INSERT INTO sessions (trainer_id, client_id, price) VALUES (?, ?, ?)", (1, 1, 50))
cur.execute("INSERT INTO sessions (trainer_id, client_id, price) VALUES (?, ?, ?)", (1, 2, 70))

connection.commit()
connection.close()
