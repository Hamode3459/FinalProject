import bcrypt
import os

USER_DATA_FILE = "users.txt"


def hash_password(plain_text_password):

    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_text_password, hashed_password):

    return bcrypt.checkpw(plain_text_password.encode('utf-8'),
                          hashed_password.encode('utf-8'))

def user_exists(username):

    if not os.path.exists(USER_DATA_FILE):
        return False

    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_username, _ = line.strip().split(',')
            if stored_username == username:
                return True
    return False

def register_user(username, password):

    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False

    hashed_pw = hash_password(password)
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f"{username},{hashed_pw}\n")

    print(f"Success: User '{username}' registered successfully!")
    return True

def login_user(username, password):

    if not os.path.exists(USER_DATA_FILE):
        print("Error: No users registered yet.")
        return False

    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_username, stored_hash = line.strip().split(',')
            if stored_username == username:
                if verify_password(password, stored_hash):
                    print(f"Success: Welcome, {username}!")
                    return True
                else:
                    print("Error: Invalid password.")
                    return False

    print("Error: Username not found.")
    return False

def display_menu():
    print("\n" + "=" * 50)
    print("  Authintication System")
    print("=" * 50)
    print("[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("=" * 50)

def main():
    print("\nWelcome to Authentication System!")

    while True:
        display_menu()
        choice = input("Please select an option (1-3): ").strip()

        if choice == '1':
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            confirm = input("Confirm password: ").strip()

            if password != confirm:
                print("Error: Passwords do not match.")
                continue

            register_user(username, password)

        elif choice == '2':
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            login_user(username, password)

        elif choice == '3':
            print("Exiting... Thanks for using the system.")
            break

        else:
            print("Invalid option, please select 1, 2, or 3.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
