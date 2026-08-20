from database.connection import get_connection
from utils.security import hash_pin, verify_pin


class Account:
    def __init__(self, name="", phone="", email="", pin=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.pin = pin

    # --------------------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------------------
    def create_account(self):
        connection = get_connection()
        if connection is None:
            return None

        cursor = connection.cursor()

        try:
            pin_hash, pin_salt = hash_pin(self.pin)

            query = """
            INSERT INTO accounts (name, phone, email, pin_hash, pin_salt)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                self.name,
                self.phone,
                self.email,
                pin_hash,
                pin_salt
            )

            cursor.execute(query, values)
            connection.commit()

            account_id = cursor.lastrowid
            return account_id

        except Exception as e:
            connection.rollback()
            print(f"Account creation error: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # LOGIN
    # --------------------------------------------------
    def login(self, account_id, pin):
        connection = get_connection()
        if connection is None:
            return None

        cursor = connection.cursor()

        try:
            query = """
            SELECT account_id, name, phone, email, pin_hash, pin_salt, balance
            FROM accounts
            WHERE account_id = %s
            """

            cursor.execute(query, (account_id,))
            account_data = cursor.fetchone()

            if account_data is None:
                return None

            stored_hash = account_data[4]
            stored_salt = account_data[5]

            if verify_pin(pin, stored_hash, stored_salt):
                return {
                    "account_id": account_data[0],
                    "name": account_data[1],
                    "phone": account_data[2],
                    "email": account_data[3],
                    "balance": float(account_data[6])
                }

            return None

        except Exception as e:
            print(f"Login error: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # CHECK BALANCE
    # --------------------------------------------------
    def check_balance(self, account_id):
        connection = get_connection()
        if connection is None:
            return None

        cursor = connection.cursor()

        try:
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            cursor.execute(query, (account_id,))
            result = cursor.fetchone()

            if result:
                return float(result[0])
            return None

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # DEPOSIT
    # --------------------------------------------------
    def deposit(self, account_id, amount):
        connection = get_connection()
        if connection is None:
            return "database_error"

        cursor = connection.cursor()

        try:
            query = "SELECT account_id FROM accounts WHERE account_id = %s"
            cursor.execute(query, (account_id,))

            if cursor.fetchone() is None:
                return "account_not_found"

            # Update balance
            query = "UPDATE accounts SET balance = balance + %s WHERE account_id = %s"
            cursor.execute(query, (amount, account_id))

            # Record transaction
            query = """
            INSERT INTO transactions (account_id, transaction_type, amount, description)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (account_id, "DEPOSIT", amount, "Cash deposited"))

            connection.commit()
            return "success"

        except Exception as e:
            connection.rollback()
            print(f"Deposit error: {e}")
            return "database_error"

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # WITHDRAW
    # --------------------------------------------------
    def withdraw(self, account_id, amount):
        connection = get_connection()
        if connection is None:
            return "database_error"

        cursor = connection.cursor()

        try:
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            cursor.execute(query, (account_id,))
            result = cursor.fetchone()

            if result is None:
                return "account_not_found"

            balance = float(result[0])

            if amount > balance:
                return "insufficient_balance"

            # Update balance
            query = "UPDATE accounts SET balance = balance - %s WHERE account_id = %s"
            cursor.execute(query, (amount, account_id))

            # Record transaction
            query = """
            INSERT INTO transactions (account_id, transaction_type, amount, description)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (account_id, "WITHDRAW", amount, "Cash withdrawn"))

            connection.commit()
            return "success"

        except Exception as e:
            connection.rollback()
            print(f"Withdrawal error: {e}")
            return "database_error"

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # TRANSFER
    # --------------------------------------------------
    def transfer(self, sender_id, receiver_id, amount):
        connection = get_connection()
        if connection is None:
            return "database_error"

        cursor = connection.cursor()

        try:
            if str(sender_id) == str(receiver_id):
                return "same_account"

            # Get sender balance
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            cursor.execute(query, (sender_id,))
            sender = cursor.fetchone()

            if sender is None:
                return "sender_not_found"

            # Check receiver
            cursor.execute(query, (receiver_id,))
            receiver = cursor.fetchone()

            if receiver is None:
                return "receiver_not_found"

            sender_balance = float(sender[0])

            if amount > sender_balance:
                return "insufficient_balance"

            # Deduct sender
            query = "UPDATE accounts SET balance = balance - %s WHERE account_id = %s"
            cursor.execute(query, (amount, sender_id))

            # Add receiver
            query = "UPDATE accounts SET balance = balance + %s WHERE account_id = %s"
            cursor.execute(query, (amount, receiver_id))

            # Record sender transaction
            tx_query = """
            INSERT INTO transactions (account_id, transaction_type, amount, description)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(tx_query, (sender_id, "TRANSFER", amount, f"Transferred to account {receiver_id}"))

            # Record receiver transaction
            cursor.execute(tx_query, (receiver_id, "TRANSFER", amount, f"Received from account {sender_id}"))

            connection.commit()
            return "success"

        except Exception as e:
            connection.rollback()
            print(f"Transfer error: {e}")
            return "database_error"

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # TRANSACTION HISTORY
    # --------------------------------------------------
    def get_transactions(self, account_id):
        connection = get_connection()
        if connection is None:
            return []

        cursor = connection.cursor()

        try:
            query = """
            SELECT transaction_id, transaction_type, amount, transaction_date, description
            FROM transactions
            WHERE account_id = %s
            ORDER BY transaction_date DESC
            """
            cursor.execute(query, (account_id,))
            return cursor.fetchall()

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # VERIFY PIN
    # --------------------------------------------------
    def verify_pin(self, account_id, pin):
        """Verifies if the provided PIN matches the account PIN in the database using salt/hash."""
        connection = get_connection()
        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            query = "SELECT pin_hash, pin_salt FROM accounts WHERE account_id = %s"
            cursor.execute(query, (account_id,))
            account_data = cursor.fetchone()

            if account_data is None:
                return False

            stored_hash = account_data[0]
            stored_salt = account_data[1]

            return verify_pin(pin, stored_hash, stored_salt)

        except Exception as e:
            print(f"Error verifying PIN: {e}")
            return False

        finally:
            cursor.close()
            connection.close()

    # --------------------------------------------------
    # CHANGE PIN
    # --------------------------------------------------
    def change_pin(self, account_id, old_pin, new_pin):
        connection = get_connection()
        if connection is None:
            return "error"

        cursor = connection.cursor()

        try:
            # 1. Verify old PIN first
            if not self.verify_pin(account_id, old_pin):
                return "invalid_old_pin"

            # 2. Hash new PIN
            new_hash, new_salt = hash_pin(new_pin)

            # 3. Update database
            query = "UPDATE accounts SET pin_hash = %s, pin_salt = %s WHERE account_id = %s"
            cursor.execute(query, (new_hash, new_salt, account_id))
            connection.commit()

            return "success"

        except Exception as e:
            connection.rollback()
            print(f"Error changing PIN: {e}")
            return "error"

        finally:
            cursor.close()
            connection.close()