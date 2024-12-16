arr = ["a", "d", "f", "s", "a", "y"]
arr_of_vowels = ["a", "e", "j", "o", "u", "y"]
counter_of_vowlels = 0

for char in arr:
    for vowel in arr_of_vowels:
        counter_of_vowlels += 1
print(counter_of_vowlels)