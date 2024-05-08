import os

user_input_path = input("Path -> ")

is_directory = os.path.isdir(user_input_path)

if is_directory:
    print(f"'{user_input_path}' is a directory.")
else:
    print(f"'{user_input_path}' is not a directory.")

