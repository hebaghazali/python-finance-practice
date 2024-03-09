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


def calculate_wacc(cost_of_equity, cost_of_debt, weight_of_equity, weight_of_debt, tax_rate):
    """
    Calculate the Weighted Average Cost of Capital (WACC) with tax rate.

    Parameters:
        cost_of_equity (float): Cost of equity (Ke).
        cost_of_debt (float): Cost of debt (Kd).
        weight_of_equity (float): Weight of equity (We).
        weight_of_debt (float): Weight of debt (Wd).
        tax_rate (float): Corporate tax rate (expressed as a decimal).

    Returns:
        float: The Weighted Average Cost of Capital (WACC) with tax rate.
    """
    wacc = ((cost_of_equity * weight_of_equity) 
            + ((cost_of_debt * (1 - tax_rate)) * weight_of_debt))
    return wacc


def evaluate_investment_project(cash_flows, wacc):
    """
    Evaluate an investment project using the Net Present Value (NPV) with WACC.

    Parameters:
        cash_flows (list): List of cash flows for each period.
        wacc (float): Weighted Average Cost of Capital (WACC).

    Returns:
        float: The Net Present Value (NPV) of the investment project.
    """
    # Calculate NPV using WACC as the discount rate
    npv = calculate_npv(cash_flows, wacc)
    return npv