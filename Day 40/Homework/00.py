def remove_duplicates(input_string):
    words = input_string.split()  # Split the string into words
    seen = set()  # Set to keep track of seen words
    result = []  # List to store the result without duplicates
    
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return ' '.join(result)  # Join the result list back into a string

# Example usage
input_string = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
output_string = remove_duplicates(input_string)
print(output_string)