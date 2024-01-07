DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS ssh_users;

CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL,
    has_llamas BOOLEAN NOT NULL
);

CREATE TABLE ssh_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    password TEXT NOT NULL
);
