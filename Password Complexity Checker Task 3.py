import re

def check_password_strength(password):
    # Initialize the strength level and feedback list
    strength = 0
    feedback = []

    # Length check: at least 8 characters
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check: at least one uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check: at least one lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Digit check: at least one digit
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Special character check: at least one special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine password strength
    if strength == 5:
        print("Password is very strong!")
    elif strength >= 3:
        print("Password is strong.")
    else:
        print("Password is weak.")

    # Print feedback
    if feedback:
        print("Feedback:")
        for suggestion in feedback:
            print(f"- {suggestion}")

def main():
    password = input("Enter a password to check its strength: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
