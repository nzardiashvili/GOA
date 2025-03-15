def divisors(integer):
    divisors_list = [i for i in range(2, integer) if integer % i == 0]
    if len(divisors_list) == 0:
        return"{integer} is prime"
    else:
        return divisors-list