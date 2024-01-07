DROP TABLE IF EXISTS credit_cards;

CREATE TABLE credit_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cardholder_name TEXT NOT NULL,
    card_number TEXT NOT NULL,
    cvv TEXT NOT NULL
);