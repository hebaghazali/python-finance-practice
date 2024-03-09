# src/simulating_mortgage_loan/plotting.py

import matplotlib.pyplot as plt

def plot_interest_vs_principal(interest_paid, principal_paid):
    """
    Plot interest vs principal payments over time.

    Parameters:
        interest_paid (array): Array containing interest payments for each period.
        principal_paid (array): Array containing principal payments for each period.
    """
    # Plot the interest vs principal
    interest_plot, = plt.plot(interest_paid, color="red", label="Interest Paid")
    principal_plot, = plt.plot(principal_paid, color="blue", label="Principal Paid")
    plt.legend(handles=[interest_plot, principal_plot], loc=2)
    plt.xlabel("Period")
    plt.ylabel("Payment Amount")
    plt.title("Interest vs Principal Payments Over Time")
    plt.grid(True)
    plt.show()
