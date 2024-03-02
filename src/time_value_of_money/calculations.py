def cumulative_growth(initial_value, growth_rate, time_period):
    """
    Calculate the cumulative growth over a period of time.

    Parameters:
        initial_value (float): The initial value of the investment or asset.
        growth_rate (float): The rate of growth (or depreciation) per period.
        time_period (int): The number of periods over which the growth is calculated.

    Returns:
        float: The cumulative growth factor.
    """
    cumulative_factor = (1 + growth_rate) ** time_period
    cumulative_value = initial_value * cumulative_factor
    return cumulative_value

def calculate_discount_factor(rate, periods):
    """
    Calculate the discount factor.

    Parameters:
        rate (float): The discount rate per period.
        periods (int): The number of periods.

    Returns:
        float: The discount factor.
    """
    discount_factor = 1 / ((1 + rate) ** periods)
    return discount_factor

def calculate_future_value_compounded(V0, r, c, t):
    """
    Calculate the future value of an investment or loan with compound interest
    considering the number of compounding periods per year.

    Parameters:
        V0 (float): Initial principal or present value.
        r (float): Annual interest rate (expressed as a decimal).
        c (int): Number of times interest is compounded per year.
        t (float): Number of years.

    Returns:
        float: The future value of the investment or loan.
    """
    compound_growth_factor = (1 + r / c) ** (t * c)
    future_value = V0 * compound_growth_factor
    return future_value


def calculate_future_value(present_value, rate, periods):
    """
    Calculate the future value of an investment with compound interest.

    Parameters:
        present_value (float): The present value of the investment.
        rate (float): The interest rate per period.
        periods (int): The number of periods.

    Returns:
        float: The future value of the investment.
    """
    future_value = present_value * ((1 + rate) ** periods)
    return future_value

def calculate_present_value(future_value, rate, periods):
    """
    Calculate the present value of a future sum of money.

    Parameters:
        future_value (float): The future value of the investment.
        rate (float): The discount rate per period.
        periods (int): The number of periods.

    Returns:
        float: The present value of the investment.
    """
    present_value = future_value * calculate_discount_factor(rate, periods)
    return present_value

