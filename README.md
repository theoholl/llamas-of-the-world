# llamas-of-the-world

TODO:

- [ ] Add database table for SSH users
- [ ] Seperate credit card details into different database file
- [ ] Add ZIP bomb or virus honeypot
- [ ] Terminate SSH connection and block IP after honeypot was downloaded

Llamas of the world (LotW) is an online service for searching countries with llamas. To access the search, one must first enter their credit card details.

The search of LotW is vulnerable to SQL injections. The machine that hosts LotW also runs a SSH server. Passwords for the SSH connection are stored in the same database as LotW.

As a trap, we stored a ZIP bomb or virus on the host machine, named 'credit-card-details.zip'.

Activate Python virtual environment:
```bash
source .venv/bin/activate
```

Initialize the database. This is only neccessary if you want to reset the current database:
```bash
python init_db.py
```

Start server in debug mode (reloads automatically when files are edited):
```bash
python -m flask --app server run --debug
```

## Test the application

Signin page requires the following inputs:

- name of credit card holder: meow
- credit card number: [any valid number](https://stripe.com/docs/testing#cards)
- cvv: any 3 digit number below 100, e.g. 042