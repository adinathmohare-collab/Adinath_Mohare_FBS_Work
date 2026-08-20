from decimal import Decimal, InvalidOperation


def get_name():
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty.")
        elif len(name) < 2:
            print("Name must contain at least 2 characters.")
        elif not all(c.isalpha() or c.isspace() for c in name):
            print("Name can contain only letters and spaces.")
        else:
            return name


def get_phone():
    while True:
        phone = input("Enter phone number: ").strip()
        if not phone.isdigit():
            print("Phone number must contain only digits.")
        elif len(phone) != 10:
            print("Phone number must contain exactly 10 digits.")
        else:
            return phone


def get_email():
    while True:
        email = input("Enter email: ").strip()
        if "@" not in email or "." not in email:
            print("Please enter a valid email.")
        else:
            return email


def get_pin(message="Enter 4-digit PIN: "):
    while True:
        pin = input(message).strip()
        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be exactly 4 digits.")
        else:
            return pin


def get_positive_amount(message):
    while True:
        try:
            amount = Decimal(input(message).strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount.as_tuple().exponent < -2:
                print("Amount can have maximum 2 decimal places.")
            else:
                return amount
        except InvalidOperation:
            print("Please enter a valid amount.")


def get_account_id():
    while True:
        account_id = input("Enter account ID: ").strip()
        if not account_id.isdigit() or int(account_id) <= 0:
            print("Invalid account ID.")
        else:
            return int(account_id)