def open_or_senior(data):
    return ["senior" if age >= 55 and handicap > 7 else "open" for age, handicap in data]