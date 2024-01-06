import sqlite3, random

connection = sqlite3.connect('database.db')

with open('db-schema.sql') as f:
    connection.executescript(f.read())

with open('countries.txt') as f:
    countries = f.readlines()
    for country in countries:
        has_llamas = random.choice([True, False])
        cur = connection.cursor()
        cur.execute("INSERT INTO countries (country_name, has_llamas) VALUES (?, ?)", (country.strip(), has_llamas))

connection.commit()
connection.close()
