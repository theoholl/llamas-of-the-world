# llamas-of-the-world

TODO:

- [ ] Add database table for SSH users
- [ ] Seperate credit card details into different database file
- [x] Add ZIP bomb or virus honeypot
- [ ] Terminate SSH connection and block IP after honeypot was downloaded

Llamas of the world (LotW) is an online service for searching countries with llamas. To access the search, one must first enter their credit card details. The search of LotW is vulnerable to SQL injections. 

The machine that hosts LotW also runs a SSH server. Passwords for the SSH connection are stored in the same database as the list of countries for the search. Credit card details are stored in a different database.

To hack this application, the hacker must use the SQL injection first to get their hand on the SSH credentials and then use those to steal the credit card details from the server.

As a trap, we stored a ZIP bomb or virus on the host machine, named 'credit-card-data.zip'.

Activate the Python virtual environment:

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

## Develop templates with TailwindCSS

First, install the required NPM packages:

```bash
npm install
```

Run the following command to start the TailwindCSS compiler and flask server. Both services will watch files for changes and update automatically.

```bash
npm run dev
```


## Test the application

Signin page requires the following inputs:

- name of credit card holder: meow
- credit card number: [any valid credit card number](https://stripe.com/docs/testing#cards)
- cvv: any 3 digit number below 100, e.g. 042

## Create a ZIP bomb

```bash
dd if=/dev/zero bs=1024 count=1000000 | zip credit-card-data -
```

`dd`: (data duplicator) copies files

`if`: input file; `/dev/zero` returns as many null characters as are read from it

`bs`: block size, how many byte are copied at a time

`count`: how many times to copy with given parameters, e.g. 1024 bytes * 1.000.000 = 1 GB when unpacked

`-`: file name of the packed file in the zip archive

