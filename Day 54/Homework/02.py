def series_sum(n):
    if n == 0:
        return "0.00"
    series_sum = sum(1 / (1 + 3 * i) for i in range(n))  
    return "{series_sum: .2f}"