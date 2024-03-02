# profitability_analysis/calculations.py

import numpy as np

def calculate_npv(cash_flows, discount_rate):
    """
    Calculate the Net Present Value (NPV) of cash flows.

    Parameters:
        cash_flows (list): List of cash flows for each period.
        discount_rate (float): Discount rate per period.

    Returns:
        float: The Net Present Value (NPV) of the cash flows.
    """
    npv = np.npv(discount_rate, cash_flows)
    return npv

# Add other profitability analysis functions here...
