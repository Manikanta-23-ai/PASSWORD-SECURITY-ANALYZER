import re


def analyze_password(password):
    score = 0
    suggestions = []

    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters (12+ is better).")

    
    has_lowercase = bool(re.search(r"[a-z]", password))
    if has_lowercase:
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    
    has_uppercase = bool(re.search(r"[A-Z]", password))
    if has_uppercase:
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    
    has_number = bool(re.search(r"\d", password))
    if has_number:
        score += 1
    else:
        suggestions.append("Add numbers.")

    
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))
    if has_special:
        score += 2
    else:
        suggestions.append("Add a special character such as @, #, $, or !.")

    
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "password123"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords.")

    
    if score <= 2:
        strength = "VERY WEAK"
    elif score <= 4:
        strength = "WEAK"
    elif score <= 6:
        strength = "MEDIUM"
    elif score <= 7:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return score, strength, suggestions, has_lowercase, has_uppercase, has_number, has_special


def main():
    print("=" * 40)
    print("     PASSWORD SECURITY ANALYZER")
    print("=" * 40)

    password = input("\nEnter a test password: ")

    (
        score,
        strength,
        suggestions,
        has_lowercase,
        has_uppercase,
        has_number,
        has_special
    ) = analyze_password(password)

    print("\n" + "-" * 40)
    print("PASSWORD ANALYSIS")
    print("-" * 40)

    print(f"Length:              {len(password)}")
    print(f"Lowercase:           {'✓' if has_lowercase else '✗'}")
    print(f"Uppercase:           {'✓' if has_uppercase else '✗'}")
    print(f"Numbers:             {'✓' if has_number else '✗'}")
    print(f"Special character:   {'✓' if has_special else '✗'}")

    print(f"\nScore: {score}/8")
    print(f"Strength: {strength}")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"• {suggestion}")
    else:
        print("\n✓ Excellent password characteristics!")

    print("-" * 40)


if __name__ == "__main__":
    main()