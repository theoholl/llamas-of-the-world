# llamas-of-the-world

Llamas of the world (LotW) is an online service for searching countries with llamas. To access the search, one must first enter their credit card details. The search of LotW is vulnerable to SQL injections. 

The machine that hosts LotW also runs a SSH server. Passwords for the SSH connection are stored in the same database as the list of countries for the search. Credit card details are stored in a different database.

To hack this application, the hacker must use the SQL injection first to get their hand on the SSH credentials and then use those to steal the credit card details from the server.

As a trap, we stored a ZIP bomb or virus on the host machine, named 'credit-card-data.zip'.

Note: `server.py` as purposefully bad error handling.

Activate the Python virtual environment:

## Installation

Install the software:

```bash
# Clone git repository
git clone https://github.com/theoholl/llamas-of-the-world
cd llamas-of-the-world/

# Install NPM dependencies
npm i

# Set up and activate python virtual environment
python -m venv .venv
source .venv/bin/activate

# Upgrade pip and install requirements
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Optional: Initialize new databases. This is only neccessary if you want to purge the current database. You can do this anytime to erase all data from the databases and start fresh.

```bash
python init_db.py
```

## Development

Activate the Python virtual environment:

```bash
source .venv/bin/activate
```

Start development server:

```bash
# Only flask server (if you don't want to edit the HTML templates)
# npm run serve

# Flask server and CSS compiler
npm run dev
```

Now you can edit Python and HTML files without having to restart the server. You only need to refresh the browser. The website will served on [http://localhost:5000](http://localhost:5000).


## Test the application

Signin page requires the following inputs:

- Name of credit card holder: meow
- Credit card number: [any valid credit card number](https://stripe.com/docs/testing#cards), e.g. 6011000990139424
- CVV: any 3 digit number below 100, e.g. 042

## Create a ZIP bomb

```bash
dd if=/dev/zero bs=1024 count=1000000 | zip credit-card-data -
```

`dd`: (data duplicator) copies files

`if`: input file; `/dev/zero` returns as many null characters as are read from it

`bs`: block size, how many byte are copied at a time

`count`: how many times to copy with given parameters, e.g. 1024 bytes * 1.000.000 = 1 GB when unpacked

`-`: file name of the packed file in the zip archive

