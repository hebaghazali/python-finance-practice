from src.time_value_of_money import (calculate_future_value_compounded, cumulative_growth,
                                  calculate_discount_factor, calculate_future_value, calculate_present_value)

# Usage example
# initial_value = 1000  # Initial value of the investment
# growth_rate = 0.1    # Growth rate (5% per period)
# time_period = 12       # Number of periods

# cumulative_value = cumulative_growth(initial_value, growth_rate, time_period)
# print("Cumulative value after {} periods: {:.2f}".format(time_period, cumulative_value))

##################################################################################

discount_rate = 0.05
periods = 5

# Usage examples
# discount_factor = calculate_discount_factor(discount_rate, periods)
# print("Discount factor for a discount rate of {} and {} periods: {:.2f}".format(discount_rate, periods, discount_factor))

##################################################################################

# initial_principal = 1000      # Initial principal or present value
# annual_interest_rate = 0.05   # Annual interest rate (5% per year)
# compounding_periods_per_year = 12  # Compounding periods per year (monthly)
# years = 5                     # Number of years

# future_value_compounded = calculate_future_value_compounded(
#     initial_principal, annual_interest_rate, compounding_periods_per_year, years)
# print("Future value with compounded interest: {:.2f}".format(future_value_compounded))

##################################################################################

future_value_example = 1276.28

# present_value = calculate_present_value(future_value_example, discount_rate, periods)
# print("Present value of a future value of {:.2f} with a discount rate of {} over {} periods: {:.2f}".format(future_value_example, discount_rate, periods, present_value))

initial_investment = 1000

# future_value = calculate_future_value(
#     initial_investment, discount_rate, periods)
# print("Future value of an initial investment of {} with a discount rate of {} over {} periods: {:.2f}".format(
#     initial_investment, discount_rate, periods, future_value))

