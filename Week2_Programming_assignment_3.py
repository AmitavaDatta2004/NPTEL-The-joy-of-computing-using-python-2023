def is_valid_password(password):
    if not (8 <= len(password) <= 32):
       return False
    elif not password[0].isalpha():
       return False
    elif any(char in '/\\=\'"' for char in password):
       return False
    elif ' ' in password:
       return False
    else:
      return True

input_string = input()

print(is_valid_password(input_string), end="")
