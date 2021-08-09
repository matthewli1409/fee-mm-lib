def get_tick_size(price: float) -> float:
    """Calculate minimum tick size based on price

    Notes:
        - Gets significant figure of each pair to calculate the min tick size
        - Example1: BTC px at 9000. min_tick_size will be 0.1
        - Example2: ETH ps at 166.0 min tick_size will be 0.01
        - Example3: LTC ps at 44.0 min tick_size will be 0.001

    Args:
        price -- i.e. 9000

    Returns:
        float: tick_size for inst
    """
    sf = 5

    # Find length of left side of decimal place. Subtract from s.f. to get multiplier
    px_s = str(price).split('.')
    if px_s[0] == '0':
        zeros = len(px_s[1]) - len(px_s[1].lstrip('0'))
        s = '0.' + str(0) * zeros + str(0) * 4 + '1'
        return float(s)
    else:
        tick_size = 1 / (10 ** (sf - len(px_s[0])))
        return tick_size
