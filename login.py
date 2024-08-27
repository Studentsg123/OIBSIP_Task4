import getpass

# Dictionary to store user credentials
users = {}

def register():
    print("Register a new user")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try a different username.")
        return
    password = getpass.getpass("Enter a password: ")
    users[username] = password
    print("User registered successfully!\n")

def login():
    print("Login to your account")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
        secured_page()
    else:
        print("Invalid username or password!\n")

def secured_page():
    print("\nWelcome to the secured page!")
    print("Only logged-in users can see this message.\n")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
