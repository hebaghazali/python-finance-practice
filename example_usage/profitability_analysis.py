
# Example cash flows and discount rate
from src.profitability_analysis.calculations import calculate_eaa, calculate_irr, calculate_npv


# Initial investment of -100, followed by positive cash flows
cash_flows = [-100, 50, 40, 30, 20, 10]
discount_rate = 0.1  # 10% discount rate

# Calculate NPV
npv = calculate_npv(cash_flows, discount_rate)
print("Net Present Value (NPV):", npv)

# Calculate IRR
irr = calculate_irr(cash_flows)
print("Internal Rate of Return (IRR):", irr)

# Calculate EAA
# Subtract 1 for the initial investment
eaa = calculate_eaa(npv, discount_rate, len(cash_flows)-1)
print("Equivalent Annual Annuity (EAA):", eaa)
