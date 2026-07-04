from core.excel_loader import ExcelLoader
from core.password_generator import PasswordGenerator

if __name__ == "__main__":
    loader = ExcelLoader("students.xlsx")
    users = loader.load_users()

    # Generate new passwords
    for user in users:
        new_pass = PasswordGenerator.generate(4)
        user["Password"] = new_pass
        print(f"Generated password for {user['Username']}: {new_pass}")

    # Save to a new file
    new_file = loader.save_new_version(users, suffix="_latest")
    print(f"✅ Passwords updated and saved to {new_file}")
