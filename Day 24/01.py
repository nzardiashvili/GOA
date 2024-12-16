def custom_join(interable, delimiter):
    result = ""
    for index, item in enumerate(iterable):
        result += item
        if index < len(interable) - 1:
            result += delimiter
            return result