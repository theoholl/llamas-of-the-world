import sqlite3, random

def initialize_countries_and_ssh_db():
    connections = sqlite3.connect('countries-and-ssh.db')

    with open('countries-and-ssh.sql') as f:
        connections.executescript(f.read())

    with open('countries.txt') as f:
        countries = f.readlines()
        for country in countries:
            has_llamas = random.choice([True, False])
            cur = connections.cursor()
            cur.execute("INSERT INTO countries (country_name, has_llamas) VALUES (?, ?)", (country.strip(), has_llamas))

    cur.execute("INSERT INTO countries (country_name, has_llamas) VALUES (?, ?)", ("Llamaland", False))

    connections.commit()
    connections.close()

def initialize_credit_cards_db():
    connection = sqlite3.connect('credit-cards.db')

    with open('credit-cards.sql') as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()

initialize_countries_and_ssh_db()
initialize_credit_cards_db()