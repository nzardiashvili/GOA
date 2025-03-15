def printer_error(s):
    return {sum(1 for char in s if char > "m")}/{len(s)}