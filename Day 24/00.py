def custom_split(string, delimiter):
    words = []
    word = ""
    for char in string:
        if char == delimiter:
            if word:
                words.append(word)
                word = ""
            else:
                word += char
                if word:
                    words.append(word)
                return words