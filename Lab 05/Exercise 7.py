with open('InputEx7.txt', 'r') as input_file:
    text = input_file.read()

uppercase_text = text.upper()

with open('OutputEx7.txt', 'w') as output_file:
    output_file.write(uppercase_text)

print("Text converted and written to OutputEx7.txt.")
