
# Example cash flows and discount rate
from src.profitability_analysis.calculations import *


# Initial investment of -100, followed by positive cash flows
# cash_flows = [-100, 50, 40, 30, 20, 10]
# discount_rate = 0.1  # 10% discount rate

# # Calculate NPV
# npv = calculate_npv(cash_flows, discount_rate)
# print("Net Present Value (NPV):", npv)

# # Calculate IRR
# irr = calculate_irr(cash_flows)
# print("Internal Rate of Return (IRR):", irr)

# # Calculate EAA
# # Subtract 1 for the initial investment
# eaa = calculate_eaa(npv, discount_rate, len(cash_flows)-1)
# print("Equivalent Annual Annuity (EAA):", eaa)

#######################################################################

# Example cash flows and weights
cash_flows = [-100, 50, 40, 30, 20, 10]  # Initial investment of -100, followed by positive cash flows
cost_of_equity = 0.10  # Cost of equity
cost_of_debt = 0.05    # Cost of debt
weight_of_equity = 0.6  # Weight of equity
weight_of_debt = 0.4    # Weight of debt
tax_rate = 0.25         # Corporate tax rate (25%)

# Calculate WACC with tax rate
wacc = calculate_wacc(cost_of_equity, cost_of_debt, weight_of_equity, weight_of_debt, tax_rate)

# Evaluate investment project using WACC
npv = evaluate_investment_project(cash_flows, wacc)
print("Net Present Value (NPV) with WACC:", npv)