def cube_odd(arr):
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in arr):
        return sum(x**3 for x in arr if x % 2 != 0)