import re
import getpass

COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "letmein",
    "admin", "iloveyou", "welcome", "monkey"
]

def check_password(password):
    is_long_enough = len(password) >= 12
    has_uppercase  = bool(re.search(r"[A-Z]", password))
    has_lowercase  = bool(re.search(r"[a-z]", password))
    has_number     = bool(re.search(r"[0-9]", password))
    has_symbol     = bool(re.search(r"[^A-Za-z0-9]", password))
    is_common      = password.lower() in COMMON_PASSWORDS

    rules  = [is_long_enough, has_uppercase, has_lowercase, has_number, has_symbol]
    passed = sum(rules)

    if is_common:
        strength, score = "Very Weak", 1
    elif passed == 5:
        strength, score = "Very Strong", 5
    elif passed == 4:
        strength, score = "Strong", 4
    elif passed == 3:
        strength, score = "Fair", 3
    elif passed == 2:
        strength, score = "Weak", 2
    else:
        strength, score = "Very Weak", 1

    tips = []
    if is_common:
        tips.append("This is a very common password. Hackers try these first!")
    if not is_long_enough:
        tips.append("Make it longer — at least 12 characters.")
    if not has_uppercase:
        tips.append("Add at least one UPPERCASE letter (e.g. A, B, C).")
    if not has_lowercase:
        tips.append("Add at least one lowercase letter (e.g. a, b, c).")
    if not has_number:
        tips.append("Add at least one number (e.g. 1, 2, 3).")
    if not has_symbol:
        tips.append("Add a special character (e.g. !, @, #, $).")
    if not tips:
        tips.append("Excellent! Save this password in a password manager.")

    return {
        "strength": strength, "score": score, "passed": passed,
        "is_long": is_long_enough, "has_upper": has_uppercase,
        "has_lower": has_lowercase, "has_number": has_number,
        "has_symbol": has_symbol, "tips": tips,
    }

def show_results(result):
    bars = {1:"[=         ]", 2:"[===       ]", 3:"[=====     ]",
            4:"[=======   ]", 5:"[==========]"}
    print()
    print("=" * 40)
    print("       PASSWORD STRENGTH REPORT")
    print("=" * 40)
    print(f"\n  Strength     : {bars[result['score']]} {result['strength']}")
    print(f"  Rules passed : {result['passed']} / 5\n")
    print("  Checklist:")
    print(f"{'✔' if result['is_long']    else '✘'}  12+ characters")
    print(f"{'✔' if result['has_upper']  else '✘'}  Uppercase letter")
    print(f"{'✔' if result['has_lower']  else '✘'}  Lowercase letter")
    print(f"{'✔' if result['has_number'] else '✘'}  Number")
    print(f"{'✔' if result['has_symbol'] else '✘'}  Special character")
    print("\n  Tips:")
    for tip in result["tips"]:
        print(f"    → {tip}")
    print("\n" + "=" * 40)

if __name__ == "__main__":
    print("\n  Welcome to the Password Strength Checker!")
    print("  (Your password is hidden as you type)\n")
    while True:
        password = getpass.getpass("  Enter a password to check (or press Enter to quit): ")
        if not password:
            print("\n  Goodbye!\n")
            break
        show_results(check_password(password))
        print()
