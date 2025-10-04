import re

def check_password_strength(password):
    strength = 0
    
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        print("Password should include at least one digit.")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("Password should include at least one uppercase letter.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print("Password should include at least one special character.")
    
    # Evaluate strength
    if strength == 4:
        print("Password strength: Strong ✅")
    elif strength == 3:
        print("Password strength: Medium ⚠️")
    else:
        print("Password strength: Weak ❌")

# Example usage
password = input("Enter a password to check: ")
check_password_strength(password)
