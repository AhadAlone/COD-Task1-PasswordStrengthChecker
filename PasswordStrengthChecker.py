import re
import math

def password_strength(password):
    strength = 0
    errors = []

    # Check password length
    if len(password) < 8:
        errors.append("Password is too short (minimum 8 characters)")
    else:
        strength += 1

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        errors.append("Password should contain at least one digit")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        errors.append("Password should contain at least one uppercase letter")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        errors.append("Password should contain at least one lowercase letter")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        errors.append("Password should contain at least one special character")

    # Calculate password entropy
    entropy = calculate_entropy(password, strength)
    if entropy < 30:
        errors.append(f"Password has low entropy: {entropy:.2f}")

    return strength, errors

# Calculate Shannon entropy
def calculate_entropy(password, strength):
    entropy = 0
    for char in password:
        prob = strength / len(password)
        entropy -= prob * math.log(prob, 2)
    return entropy

# Convert entropy into strength percentage
def entropy_to_strength_percentage(entropy):
    entropy_ranges = [
        (0, 0.99),
        (1, 1.99),
        (2, 2.99),
        (3, 3.99),
        (4, 4.99),
        (5, 5.99),
        (6, 6.99),
        (7, 7.99),
        (8, 8.99),
        (9, 10)
    ]

    for i, (low, high) in enumerate(entropy_ranges):
        if low <= entropy <= high:
            break

    strength_percentage = (entropy - low) / (high - low) * 100

    return strength_percentage

def get_password_strength_message(strength):
    if strength == 0:
        return "Very Weak"
    elif strength == 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    elif strength == 4:
        return "Very Strong"
    elif strength == 5:
        return "Very Very Strong"
    else:
        return "No Password"

def main():
    password = input("Enter Password: ")
    strength, errors = password_strength(password)
    entropy = calculate_entropy(password, strength)
    print("\nPassword strength:", get_password_strength_message(strength), "\n")

    if errors:
        print(",\n ".join(errors), "\n")
    
    if strength > 4:
        print("Strength: ", round(entropy_to_strength_percentage(entropy), 2), "%")

if __name__ == "__main__":
    main()
