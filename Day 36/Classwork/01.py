def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
word1 = input("შეიყვანეტ პირველი სიტყვა: ")
word2 = input("შეიყვანეტ მეორე სიტყვა: ")
if is_anagram(word1, word2):
    print("{word1} და {word2}")
    print("{word1} და {word2}")

