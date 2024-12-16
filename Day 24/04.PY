def custom_input_join():
    num_words = int(input("Enter the number of words: "))
    words = []
    for _ in range(num_words):
        words = input("Enter a word: ")
        words.append(words)
        result = custom_input_join(words, "")
        print("joined words:, result")