DROP TABLE IF EXISTS trainers;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS sessions;

CREATE TABLE trainers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    trainer_id INTEGER,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id)
);

CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trainer_id INTEGER,
    client_id INTEGER,
    price REAL,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id),
    FOREIGN KEY (client_id) REFERENCES clients (id)
);
