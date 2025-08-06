import getpass
import sys

def main():
    vault = {}

    while True:
        print("-" * 30)
        print("\n🔐 Password Vault")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Show All Websites")
        print("4. Exit")
        print("-" * 30)
        opt = input(">> ")

        try:
            opt = int(opt)
        except ValueError:
            print("Please enter a valid number (1–4).")
            continue

        if opt == 1:
            add_password(vault)
        elif opt == 2:
            retrieve_password(vault)
        elif opt == 3:
            show_all_websites(vault)
        elif opt == 4:
            print("Goodbye!")
            sys.exit()
        else:
            print("Choose between 1–4.")

def add_password(vault):
    web = input("Enter website name: ").lower()
    web_pass = getpass.getpass("Enter Password: ")
    # web_pass = input("Enter Password: ")
    vault[web] = web_pass
    print(f"✅ Password saved for {web}.")

def retrieve_password(vault):
    get_web = input("Enter website to retrieve password: ").lower()
    try:
        print(f"🔑 Password for {get_web}: {vault[get_web]}")
    except KeyError:
        print("❌ No password found for this website.")

def show_all_websites(vault):
    if not vault:
        print("No websites saved yet.")
        return
    print("\n🌐 Stored Websites:")
    for website in vault:
        print(f"• {website}")

main()
