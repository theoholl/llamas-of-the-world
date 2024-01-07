from flask import Flask, request, redirect, render_template
import sqlite3
from validation import CreditCardValidator as validator

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('credit-card.html')
    else:
        cardholder_name = request.form["cardholder_name"]
        card_number = request.form["card_number"]
        cvv = request.form["cvv"]

        try:
            if (validator.validate_card_number(card_number) and validator.validate_cardholder_name(cardholder_name) and validator.validate_cvv(cvv)):
                connection = sqlite3.connect('credit-cards.db')
                cur = connection.cursor()
                cur.execute("INSERT INTO credit_cards (cardholder_name, card_number, cvv) VALUES (?, ?, ?)",
                            (cardholder_name, card_number, cvv))
                connection.commit()
                connection.close()
                return redirect("/llamas-of-the-world")
            else:
                return redirect("/")
        except Exception as ex:
            return f"<pre>{ex}</pre>"


@app.route("/llamas-of-the-world", methods=['GET'])
def lotw():
    country = request.args.get("country")
    has_llamas = None

    if country:
        try:
            connection = sqlite3.connect('countries-and-ssh.db')
            cur = connection.cursor()

            # Vulnerable to SQL injections
            result = cur.execute(
                f"SELECT * FROM countries WHERE country_name = '{country}'").fetchall()
            has_llamas = bool(result[0][2])
        except Exception as ex:
            return f"<pre>{ex}</pre>"

    # Return template
    return render_template('llamas-of-the-world.html', has_llamas=has_llamas, country=country)
