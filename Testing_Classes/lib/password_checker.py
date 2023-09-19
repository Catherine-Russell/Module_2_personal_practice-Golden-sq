# File: lib/password_checker.py

class PasswordChecker:
    def check(self, password):
        if password.isspace():
            raise Exception("Password cannot be empty space.")
        elif len(password) < 8:
            raise Exception("Invalid password, must be 8+ characters.")
        elif password.isalpha() or password.isdigit():
            raise Exception("Password must contain letters and numbers")
        special_chars = ["!","@","£","$","&","*"]
        for char in special_chars:
            if char in password:
                return True
        raise Exception("Password must contain a special character")