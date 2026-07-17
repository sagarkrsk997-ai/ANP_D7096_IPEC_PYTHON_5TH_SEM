# Function to check password strength

def check_password(password):
    upper = False
    lower = False
    digit = False

    if len(password) >= 8:
        for ch in password:
            if ch.isupper():
                upper = True
            elif ch.islower():
                lower = True
            elif ch.isdigit():
                digit = True

        if upper and lower and digit:
            return "Strong Password"

    return "Weak Password"


# Main Program
password = input("Enter Password: ")

result = check_password(password)

print(result)