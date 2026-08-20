from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.account import Account

app = Flask(__name__)
app.secret_key = "bank_management_secret_key_change_this"

# --------------------------------------------------
# HOME & AUTHENTICATION ROUTES
# --------------------------------------------------

@app.route("/")
def index():
    if "account_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        pin = request.form.get("pin")

        if not all([name, phone, email, pin]):
            flash("All fields are required.", "warning")
            return render_template("register.html")

        try:
            account = Account(name=name, phone=phone, email=email, pin=pin)
            account_id = account.create_account()

            if account_id:
                flash(f"Account created successfully! Your Account ID is: {account_id}", "success")
                return redirect(url_for("login"))
            else:
                flash("Account creation failed. Email or phone may already exist.", "danger")

        except Exception as e:
            print(f"\n--- REGISTER EXCEPTION: {e} ---\n")
            flash(f"Database error during registration: {e}", "danger")
            return render_template("register.html")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        account_id = request.form.get("account_id")
        pin = request.form.get("pin")

        if not account_id or not pin:
            flash("Please fill in both Account ID and PIN.", "warning")
            return render_template("login.html")

        try:
            account = Account()
            account_data = account.login(account_id, pin)

            if account_data:
                session["account_id"] = account_data["account_id"]
                session["name"] = account_data["name"]
                flash("Logged in successfully!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid Account ID or PIN.", "danger")
                return render_template("login.html")

        except Exception as e:
            print(f"\n--- LOGIN EXCEPTION: {e} ---\n")
            flash(f"Database/Server error during login: {e}", "danger")
            return render_template("login.html")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))

# --------------------------------------------------
# BANK OPERATIONAL ROUTES
# --------------------------------------------------

@app.route("/dashboard")
def dashboard():
    if "account_id" not in session:
        return redirect(url_for("login"))

    account = Account()
    balance = account.check_balance(session["account_id"]) or 0.0

    return render_template(
        "dashboard.html", name=session.get("name"), balance=balance
    )

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if "account_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            amount = float(request.form.get("amount"))
            if amount <= 0:
                flash("Amount must be greater than 0.", "warning")
                return render_template("deposit.html")

            account = Account()
            result = account.deposit(session["account_id"], amount)

            if result == "success":
                flash(f"₹{amount:.2f} deposited successfully!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Deposit failed.", "danger")
        except (ValueError, TypeError):
            flash("Please enter a valid amount.", "danger")

    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "account_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        amount = request.form.get("amount")
        pin = request.form.get("pin")

        if not amount or not pin:
            flash("Please enter both amount and PIN.", "warning")
            return render_template("withdraw.html")

        account = Account()
        
        # Verify PIN
        if not account.verify_pin(session["account_id"], pin):
            flash("Incorrect Security PIN.", "danger")
            return render_template("withdraw.html")

        # Process withdrawal
        result = account.withdraw(session["account_id"], float(amount))

        if result == "success":
            flash(f"Withdrawal of ₹{amount} was successful!", "success")
        elif result == "insufficient_balance":
            flash("Insufficient account balance.", "danger")
        elif result == "account_not_found":
            flash("Account not found.", "danger")
        else:
            flash("Database error occurred while processing withdrawal.", "danger")

        return render_template("withdraw.html")

    return render_template("withdraw.html")

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if "account_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        receiver_id = request.form.get("receiver_id")
        try:
            amount = float(request.form.get("amount"))
            if amount <= 0:
                flash("Amount must be greater than 0.", "warning")
                return render_template("transfer.html")

            account = Account()
            result = account.transfer(session["account_id"], receiver_id, amount)

            if result == "success":
                flash(f"₹{amount:.2f} transferred successfully!", "success")
                return redirect(url_for("dashboard"))
            elif result == "same_account":
                flash("You cannot transfer money to your own account.", "warning")
            elif result == "receiver_not_found":
                flash("Receiver account not found.", "danger")
            elif result == "insufficient_balance":
                flash("Insufficient balance.", "danger")
            else:
                flash("Transfer failed.", "danger")
        except (ValueError, TypeError):
            flash("Please enter a valid amount.", "danger")

    return render_template("transfer.html")

@app.route("/transactions")
def transactions():
    if "account_id" not in session:
        return redirect(url_for("login"))

    account = Account()
    history = account.get_transactions(session["account_id"])
    return render_template("transactions.html", transactions=history)

@app.route("/change-pin", methods=["GET", "POST"])
def change_pin():
    if "account_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        old_pin = request.form.get("old_pin")
        new_pin = request.form.get("new_pin")
        confirm_pin = request.form.get("confirm_pin")

        if len(new_pin) != 4 or not new_pin.isdigit():
            flash("New PIN must be exactly 4 digits.", "warning")
            return render_template("change_pin.html")

        if new_pin != confirm_pin:
            flash("New PIN and Confirm PIN do not match.", "danger")
            return render_template("change_pin.html")

        account = Account()
        result = account.change_pin(session["account_id"], old_pin, new_pin)

        if result == "success":
            flash("PIN changed successfully!", "success")
            return redirect(url_for("dashboard"))
        elif result == "invalid_old_pin":
            flash("Current PIN is incorrect.", "danger")
        else:
            flash("Failed to change PIN. Please try again.", "danger")

    return render_template("change_pin.html")

if __name__ == "__main__":
    app.run(debug=True)