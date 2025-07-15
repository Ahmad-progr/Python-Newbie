balance = 1000

def main():
    global balance
    
    if valid_pin():
        while True:
            print("\n=======================================")
            print("Welcome to Python Bank ATM")
            print("=======================================\n")
            print("1. 🧾 Check balance")
            print("2. 💰 Deposit cash")
            print("3. 💸 Withdraw cash")
            print("4. 🚪 Exit")
            print("=======================================\n")

            opt = valid_option()
            
            match opt:
                case 1:
                    print(f"\n🧾 Current Balance: ${balance:,}")
                case 2:
                    new_balance = deposit(balance)
                    if new_balance is not None:
                        print(f"\n✅ Deposit Successful!\n💰 New Balance: ${new_balance:,}")
                        balance = new_balance
                case 3:
                    new_balance = withdraw(balance)
                    if new_balance is not None:
                        print(f"\n✅ Withdrawal Successful!\n💸 New Balance: ${new_balance:,}")
                        balance = new_balance
                case 4:
                    print("\n🚪 Exiting... Thank you for using Python Bank!\n")
                    break

def valid_option():
    while True:
        opt = input("Choose an option (1-4): ")

        if opt.isdigit() and opt in '1234':
            return int(opt)
        
        print("⚠️  Choose a valid option between 1 and 4.\n")





def valid_pin():
    while True:
        pin = input("🔐 Input 4-digit pin: ")

        if pin.isdigit() and len(pin) == 4:
            print("✅ Access granted!")
            return True
        
        else:
            print("❌ Invalid PIN! Please enter a 4-digit number.\n")




def deposit(balance):  
    while True:
        cash = input("💵 How much do you want to deposit? $")

        try:
            cash = int(cash)

            if cash <= 0:
                print("⚠️  Deposit amount must be greater than zero.\n")
                continue

            return balance + cash
        
        except ValueError:
            print("⚠️  Please input a valid amount in numbers!\n")




def withdraw(balance):
    if balance == 0:
        print("⚠️  Your balance is $0. Nothing to withdraw.\n")
        return None

    while True:
        cash = input("💸 How much do you want to withdraw? $")
        
        try:
            cash = int(cash)

            if cash <= 0:
                print("⚠️  Withdraw amount must be greater than zero.\n")
                continue

            if cash > balance:
                print(f"❌ Not enough balance! You have ${balance:,}\n")
                continue

            return balance - cash
        
        except ValueError:
            print("⚠️  Please enter a valid numeric amount.\n")



main()
