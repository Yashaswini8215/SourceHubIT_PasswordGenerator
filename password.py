import random
import string

# Try to import pyperclip for clipboard functionality (optional)
try:
    import pyperclip
    CLIPBOARD = True
except ImportError:
    CLIPBOARD = False


def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    """
    Generate a strong random password based on user preferences.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Base character set (always lowercase letters)
    char_set = string.ascii_lowercase

    if use_upper:
        char_set += string.ascii_uppercase
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("No character sets selected! Please enable at least one option.")

    # Ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))  # always at least one lowercase

    # Fill remaining slots with random choices
    while len(password) < length:
        password.append(random.choice(char_set))

    # Shuffle to remove predictability
    random.shuffle(password)

    return ''.join(password)


# Main program
if __name__ == "__main__":
    print("🔐 Custom Random Password Generator 🔐")

    length = int(input("Enter desired password length: "))

    # Optional user preferences
    use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_symbols = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    try:
        password = generate_password(length, use_upper, use_numbers, use_symbols)
        print("\n✅ Generated Secure Password:", password)

        # Copy to clipboard if pyperclip available
        if CLIPBOARD:
            pyperclip.copy(password)
            print("📋 Password copied to clipboard!")
        else:
            print("ℹ️ Install 'pyperclip' module to enable clipboard copy (pip install pyperclip).")

    except ValueError as e:
        print("❌ Error:", e)
