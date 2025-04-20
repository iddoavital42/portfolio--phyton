import os

FILENAME = "passwords.txt"

def add_password():
    service = input("Service name: ")
    username = input("Username: ")
    password = input("Password: ")

    with open(FILENAME, "a") as file:
        file.write(f"{service},{username},{password}\n")

    print("✅ Password saved!")

def view_passwords():
    if not os.path.exists(FILENAME):
        print("📭 No saved passwords.")
        return

    print("\n🔐 Saved Passwords:")
    with open(FILENAME, "r") as file:
        for line in file:
            service, username, password = line.strip().split(",")
            print(f"🔹 {service}: {username} | {password}")

def search_password():
    query = input("Enter service name to search: ").lower()
    found = False

    with open(FILENAME, "r") as file:
        for line in file:
            service, username, password = line.strip().split(",")
            if service.lower() == query:
                print(f"\n🔍 Found:\n{service}: {username} | {password}")
                found = True
                break

    if not found:
        print("❌ Service not found.")

def main():
    while True:
        print("\n🧠 Password Manager")
        print("1. Add new password")
        print("2. View all passwords")
        print("3. Search by service")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
