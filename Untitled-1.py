def capitalize_words(input_string):
    # Split the string into words, capitalize each word, and then join them back
    result_string = ' '.join(word.capitalize() for word in input_string.split())
    return result_string

# Example usage:
input_string = input("Enter a string: ")
print(capitalize_words(input_string))
