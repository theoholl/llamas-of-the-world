from flask import Flask, request, redirect, render_template
import sqlite3
from validation import CreditCardValidator as validator

app = Flask(__name__)

# User details


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('user.html')
    else:
        name = request.form["name"]
        credit_card_number = request.form["credit_card_number"]
        cvv = request.form["cvv"]

        try:
            if (validator.validate_card_number(credit_card_number) and validator.validate_cardholder_name(name) and validator.validate_cvv(cvv)):
                connection = sqlite3.connect('database.db')
                cur = connection.cursor()
                cur.execute("INSERT INTO users (name, credit_card_number, cvv) VALUES (?, ?, ?)",
                            (name, credit_card_number, cvv))
                connection.commit()
                connection.close()
        except Exception as ex:
            return f"<pre>{ex}</pre>"

        return redirect("/lotwie")


@app.route("/lotwie", methods=['GET'])
def lotw():
    country = request.args.get("country")
    has_llamas = None

    if country:
        try:
            connection = sqlite3.connect('database.db')
            cur = connection.cursor()

            # Vulnerable to SQL injections
            result = cur.execute(
                f"SELECT * FROM countries WHERE country_name = '{country}'").fetchall()
            has_llamas = bool(result[0][2])
        except Exception as ex:
            return f"<pre>{ex}</pre>"

    # Return template
    return render_template('./lotw.html', has_llamas=has_llamas, country=country)
