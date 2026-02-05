def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    pcts = []
    i = 1
    while i < (len(series)):
        if series[i - 1] == 0:
            pct = 0.0
            pcts.append(pct)
            i+=1
            continue
        pct = (series[i] - series[i-1]) / series[i-1]
        pcts.append(pct)
        i+=1
    return pcts
 