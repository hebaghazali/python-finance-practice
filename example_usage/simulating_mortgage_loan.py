from src.simulating_mortgage_loan import *

# Example inputs
principal = 200000       # Loan amount
annual_interest_rate = 0.04  # Annual interest rate (4%)
loan_term_years = 30    # Loan term in years

# Calculate monthly mortgage payment
monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term_years)
print("Monthly Mortgage Payment:", monthly_payment)
