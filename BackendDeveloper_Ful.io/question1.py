import re

def is_valid_contact_number(number):
    # Regular expression pattern for valid contact numbers
    pattern = r'^(\+)?(\d{1,3})?[ -.]?\(?\d{3}\)?[ -.]?\d{3}[ -.]?\d{4}$'
    
    if re.match(pattern, number):
        return True
    else:
        return False

# Test the function with different examples
test_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for number in test_numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")

# Allow the user to test multiple numbers
while True:
    user_number = input("Enter a contact number to test (or 'n' to quit): ")
    if user_number.lower() == 'n':
        break
    if is_valid_contact_number(user_number):
        print(f"{user_number} is a valid contact number.")
    else:
        print(f"{user_number} is an invalid contact number.")
