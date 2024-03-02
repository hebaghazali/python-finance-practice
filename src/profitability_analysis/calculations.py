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

def calculate_irr(cash_flows):
    """
    Calculate the Internal Rate of Return (IRR) of cash flows.

    Parameters:
        cash_flows (list): List of cash flows for each period.

    Returns:
        float: The Internal Rate of Return (IRR) of the cash flows.
    """
    irr = np.irr(cash_flows)
    return irr


def calculate_eaa(npv, discount_rate, periods):
    """
    Calculate the Equivalent Annual Annuity (EAA) of an investment.

    Parameters:
        npv (float): Net Present Value (NPV) of the cash flows.
        discount_rate (float): Discount rate per period.
        periods (int): Total number of periods.

    Returns:
        float: The Equivalent Annual Annuity (EAA) of the investment.
    """
    annuity_factor = discount_rate / (1 - (1 + discount_rate) ** -periods)
    eaa = npv / annuity_factor
    return eaa