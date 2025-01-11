def custom_join(words, delimiter):
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i < len(words) - 1:
            result += delimiter
    return result

words = ["hello", "words", "this", "python"]
print("ccostom_words")
