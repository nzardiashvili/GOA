def row_sum_odd_numbers(n):
    start = n * n-(n - 1)
    return n * (start + start + 2 * (n - 1)) // 2