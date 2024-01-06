from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# User details
@app.route("/")
def index():
    f = open('user.html')
    content = f.read()
    f.close()
    return content

@app.route("/lotwie", methods=['GET'])
def lotw():
    country = request.args.get("country")
    has_llamas = None

    if country:
        connection = sqlite3.connect('database.db')
        cur = connection.cursor()
        result = cur.execute(f"SELECT * FROM countries WHERE country_name = '{country}'").fetchall()
        has_llamas =  bool(result[0][2])
        
    # Return template
    return render_template('./lotw.html', has_llamas=has_llamas, country=country)

@app.route("/credit-card", methods=['POST'])
def save_user():
    name = request.form["name"]
    credit_card_number = request.form["credit_card_number"]
    cvv = request.form["cvv"]

    try:
        if (validate_credit_card(credit_card_number) and validate_user_name(name) and validate_cvv(cvv)):
            connection = sqlite3.connect('database.db')
            cur = connection.cursor()
            cur.execute("INSERT INTO users (name, credit_card_number, cvv) VALUES (?, ?, ?)", (name, credit_card_number, cvv))
            connection.commit()
            connection.close()
    except Exception as ex:
        return f"<p>{ex}</p>"
    
    return redirect("/lotwie")


def validate_credit_card(card_number: str) -> bool:
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)

    # 8. If checkSum is divisible by 10, it is valid.
    return checkSum % 10 == 0

def validate_user_name(name: str) -> bool:
    """This function validates a cardholder name."""
    if "meow" not in name:
        return False
    return True

def validate_cvv(cvv: str) -> bool:
    """This function validated the card cvv"""
    if len(cvv) == 3 and cvv.isnumeric() and int(cvv) < 100:
        return True
    return False
