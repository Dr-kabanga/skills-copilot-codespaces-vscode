import re
import pyotp

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, username, password):
        if self.check_password_strength(password):
            self.passwords[username] = password
            print("Password successfully added.")
        else:
            print("Password is too weak. Please use a stronger password.")

    def check_password_strength(self, password):
        # Check password strength using regex and length
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    def export_passwords(self, file_path):
        with open(file_path, 'w') as file:
            for username, password in self.passwords.items():
                file.write(f'{username},{password}\n')
        print("Passwords exported securely.")

    def generate_mfa_code(self, secret_key):
        totp = pyotp.TOTP(secret_key)
        return totp.now()

# Example usage
manager = PasswordManager()
manager.add_password("user1", "StrongPass123!")
print("MFA Code:", manager.generate_mfa_code("BASE32SECRET"))