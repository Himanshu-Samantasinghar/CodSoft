import random
import string

def generate_password(length, special_chars, numbers, uppercase):
    # Define character sets
    chars_lower = string.ascii_lowercase
    chars_upper = string.ascii_uppercase if uppercase else ""
    chars_special = string.punctuation if special_chars else ""
    chars_numbers = string.digits if numbers else ""

    # Combine character sets
    all_chars = chars_lower + chars_upper + chars_special + chars_numbers

    # Ensure password length is at least the sum of chosen categories
    min_length = special_chars + numbers + uppercase
    if length < min_length:
        length = min_length

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    special_chars = input("Do you want to include special characters? (yes/no): ").lower() == "yes"
    numbers = input("Do you want to include numbers? (yes/no): ").lower() == "yes"
    uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == "yes"

    password = generate_password(length, special_chars, numbers, uppercase)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
