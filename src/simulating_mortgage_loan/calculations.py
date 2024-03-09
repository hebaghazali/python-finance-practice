def calculate_monthly_payment(principal, annual_interest_rate, loan_term_years):
    """
    Calculate the monthly mortgage payment for a fixed-rate mortgage loan.

    Parameters:
        principal (float): The loan amount or principal.
        annual_interest_rate (float): Annual interest rate (expressed as a decimal).
        loan_term_years (int): Loan term in years.

    Returns:
        float: The monthly mortgage payment.
    """
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = annual_interest_rate / 12

    # Convert loan term to months
    loan_term_months = loan_term_years * 12

    # Calculate monthly payment using the formula for fixed-rate mortgage
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term_months)
    return monthly_payment
