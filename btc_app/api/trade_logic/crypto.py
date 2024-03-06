def cash_to_dispatch(cash: float, number_of_investments: int) -> float:
    """Returns the amount of cash available to dispatch for a Crypto currency coin.
    
    The amount of cash available to dispatch for a Crypto currency coin is determined by dividing 
    the total amount of cash available by the number of coins in the portfolio. If the total amount
    available is less than $50.00 USD, then the total amount available is returned.

    Args:
        cash (float): The amount of cash available.
        number_of_investments (int): The number of investments held; Ex: If 3 stocks (coins) are held, then the number_of_investments = 3.

    Returns:
        float: The amount of cash available to dispatch, if the total amount available is greater than $50.00 USD, else total.
    """
    if cash < 50.00:
        return cash
    else:
        return cash / number_of_investments
