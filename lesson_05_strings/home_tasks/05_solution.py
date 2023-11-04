input_string = input("Enter a text: ")
print(input_string)
formatted_string = input_string[:3].upper() + input_string[3:-3].lower() + input_string[-3:].upper()
print(formatted_string)
