def calculate_mortgage(principal, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / 12 / 100
    number_of_payments = loan_term * 12

    # Monthly mortgage payment formula
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    return round(monthly_payment, 2)