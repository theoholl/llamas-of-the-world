# llamas-of-the-world

Llamas of the world (LotW) is an online service for searching countries with llamas. To access the search, one must first enter their credit card details.

The search of LotW is vulnerable to SQL injections. The machine that hosts LotW also runs a SSH server. Passwords for the SSH connection are stored in the same database as LotW.

As a trap, we stored a ZIP bomb or virus on the host machine, named 'credit-card-details.zip'.

Optional: A script is watching the ZIP file to be opened. When it's opened, it blocks the IP of the machine that is currently connected to SSH.

Activate Python virtual environment:
```bash
source .venv/bin/activate
```

Initialize the database:
```bash
python init_db.py
```

Start server in debug mode (reloads automatically when files are edited):
```bash
python -m flask --app server run --debug
```