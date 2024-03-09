from src.simulating_mortgage_loan import calculations, plotting

# # Example inputs
# principal = 200000       # Loan amount
# annual_interest_rate = 0.04  # Annual interest rate (4%)
# loan_term_years = 30    # Loan term in years

# # Calculate monthly mortgage payment
# monthly_payment = calculations.calculate_monthly_payment(principal, annual_interest_rate, loan_term_years)
# print("Monthly Mortgage Payment:", monthly_payment)



# Set up variables
mortgage_loan = 300000  # Initial mortgage loan amount
mortgage_rate_annual = 0.04  # Annual mortgage interest rate (4%)
mortgage_term_years = 30  # Mortgage term in years
periods_per_year = 12  # Number of payment periods per year

# Calculate mortgage payments
interest_paid, principal_paid, _ = calculations.calculate_mortgage_payments(mortgage_loan, mortgage_rate_annual, mortgage_term_years, periods_per_year)

# Plot the interest vs principal payments
plotting.plot_interest_vs_principal(interest_paid, principal_paid)