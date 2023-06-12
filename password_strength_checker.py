import string

def check_password_strength(password):
    length = len(password)
    has_digits = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbols = any(char in string.punctuation for char in password)

    if length <= 10 and has_digits:
        return "EXTREMELY BAD", "Having just numbers will make your password weak. You should add an uppercase and lowercase letter, as well as a symbol, somewhere to make your password more secure."
    elif length <= 17 and has_digits:
        return "VERY BAD", "Having just numbers will make your password weak. You should add an uppercase and lowercase letter, as well as a symbol, somewhere to make your password more secure."
    elif length >= 18 and has_digits:
        return "BAD", "Having just numbers will make your password weak. You should add an uppercase and lowercase letter, as well as a symbol, somewhere to make your password more secure."

    if length <= 12 and has_lower:
        return "EXTREMELY BAD", "Having just letters is still a security flaw. You should add uppercase and lowercase letters, as well as a symbol, somewhere to make your password more secure."
    elif length <= 14 and has_lower:
        return "BAD", "Having just letters is still a security flaw. You should add uppercase and lowercase letters, as well as a symbol, somewhere to make your password more secure."
    elif length == 15 and has_lower:
        return "OKAY", "Having just letters is still a security flaw. You should add uppercase and lowercase letters, as well as a symbol, somewhere to make your password more secure."

    if length <= 9 and has_lower and has_upper:
        return "EXTREMELY BAD", "Having upper and lowercase letters is good, but you are still vulnerable to common attacks. You should add a number and symbol."
    elif length <= 11 and has_lower and has_upper:
        return "BAD", "Having upper and lowercase letters is good, but you are still vulnerable to common attacks. You should add a number and symbol."
    elif length >= 12 and has_lower and has_upper:
        return "OKAY", "Having upper and lowercase letters is good, but you are still vulnerable to common attacks. You should add a number and symbol."

    if length <= 9 and has_lower and has_upper and has_digits:
        return "EXTREMELY BAD", "You should consider making your password longer or try adding a symbol to enhance its security."
    elif length <= 11 and has_lower and has_upper and has_digits:
        return "BAD", "You should consider making your password longer or try adding a symbol to enhance its security."
    elif length >= 12 and has_lower and has_upper and has_digits:
        return "GOOD", "You should consider making your password longer or try adding a symbol to enhance its security."

    if length <= 8 and has_lower and has_upper and has_digits and has_symbols:
        return "EXTREMELY BAD", "You should make your password longer. It is still vulnerable to common attacks."
    elif length <= 11 and has_lower and has_upper and has_digits and has_symbols:
        return "BAD", "You should make your password longer. It is still vulnerable to common attacks."
    elif length >= 12 and has_lower and has_upper and has_digits and has_symbols:
        return "GOOD", "You should make your password longer. It is still vulnerable to common attacks."

    return "UNKNOWN", "Unable to determine password strength."

while True:
    password = input("Enter a password: ")
    if password.lower() == 'exit':
        break

    strength, recommendation = check_password_strength(password)
    print("Password strength:", strength)
    print("Recommendation:", recommendation)
    print()
