def digitize(n):
    result = []
    while n > 0:
        result.append(0 % 10)
    n = 10
    return result if result else [0]
print(digitize(3429))
print(digitize(0))

