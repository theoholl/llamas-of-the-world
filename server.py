from flask import Flask, request, redirect, render_template, Response
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
    return render_template('llamas-of-the-world.html')

@app.route("/search-for-llamas", methods=['GET'])
def search_for_llamas():
    country = request.args.get("country")
    if country is None:
        return Response(
            "{'Error': 'Query parameter \'country\' missing.'}", 
            status=400, 
            mimetype='application/json'
        )
    
    try:
        connection = sqlite3.connect('countries-and-ssh.db')
        db_cursor = connection.cursor()

        # This way of querying the database is vulnerable to SQL injections!!
        result = db_cursor.execute(
            f"SELECT * FROM countries WHERE country_name = '{country}'"
        ).fetchall()

        print(result)
        return result
    
    except Exception as exception:
        return exception
