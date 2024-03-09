import numpy as np


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


def calculate_mortgage_payments(mortgage_loan, mortgage_rate_annual, mortgage_term_years, periods_per_year):
    """
    Calculate mortgage payments over time.

    Parameters:
        mortgage_loan (float): Initial mortgage loan amount.
        mortgage_rate_annual (float): Annual mortgage interest rate (expressed as a decimal).
        mortgage_term_years (int): Mortgage term in years.
        periods_per_year (int): Number of payment periods per year.

    Returns:
        tuple: Tuple containing arrays for interest, principal paid, and principal remaining.
    """
    # Calculate periodic mortgage rate and total number of payment periods
    mortgage_rate_periodic = mortgage_rate_annual / periods_per_year
    mortgage_payment_periods = mortgage_term_years * periods_per_year

    # Calculate periodic mortgage payment using the formula for a fixed-rate mortgage
    periodic_mortgage_payment = (mortgage_loan * mortgage_rate_periodic) / (1 - (1 + mortgage_rate_periodic) ** -mortgage_payment_periods)

    # Initialize arrays to store interest, principal paid, and principal remaining for each period
    interest_paid = np.zeros(mortgage_payment_periods)
    principal_paid = np.zeros(mortgage_payment_periods)
    principal_remaining = np.zeros(mortgage_payment_periods)

    # Loop through each mortgage payment period
    for i in range(0, mortgage_payment_periods):
        
        # Handle the case for the first iteration
        if i == 0:
            previous_principal_remaining = mortgage_loan
        else:
            previous_principal_remaining = principal_remaining[i-1]
            
        # Calculate the interest based on the previous principal
        interest_payment = round(previous_principal_remaining * mortgage_rate_periodic, 2)
        principal_payment = round(periodic_mortgage_payment - interest_payment, 2)
        
        # Catch the case where all principal is paid off in the final period
        if previous_principal_remaining - principal_payment < 0:
            principal_payment = previous_principal_remaining
            
        # Collect the historical values
        interest_paid[i] = interest_payment
        principal_paid[i] = principal_payment
        principal_remaining[i] = previous_principal_remaining - principal_payment

    return interest_paid, principal_paid, principal_remaining