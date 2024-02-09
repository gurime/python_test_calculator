from flask import Flask, Blueprint, render_template, request
from utlis import calculate_mortgage

app = Flask(__name__)

views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/calculate', methods=['POST'])
def calculate():
    if 'reset_button' in request.form:
        # Reset button clicked, set monthly_payment to 0
        monthly_payment = 0
    else:
        # Calculate monthly payment
        principal = float(request.form['principal'])
        interest_rate = float(request.form['interestRate']) / 100
        loan_term = int(request.form['loanTerm'])
        monthly_payment = calculate_mortgage(principal, interest_rate, loan_term)

    return render_template('index.html', monthly_payment=monthly_payment)
