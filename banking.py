attempt = 0
correct_pin = 5050
balance = 5000

while attempt < 3:
    pin = int(input("Enter your Atm PIN: "))
    
    if pin == correct_pin:
        print("Welcome to Nikhil Bank!")
        
        while True:
            print("""
            1. Deposit
            2. Withdraw
            3. Balance Check
            4. Exit
            """)
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                deposit = float(input("Enter the amount to deposit: "))
                if deposit > 0:
                    balance += deposit
                    print(f"₹{deposit} deposited successfully. New balance: ₹{balance}")
                else:
                    print("Invalid amount.")
            
            elif choice == 2:
                withdraw = float(input("Enter the amount to withdraw: "))
                if withdraw > 0:
                    if withdraw <= balance:
                        balance -= withdraw
                        print(f"₹{withdraw} withdrawn successfully. New balance: ₹{balance}")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Invalid amount.")
            
            elif choice == 3:
                print(f"Your current balance is ₹{balance}")
            
            elif choice == 4:
                print("Thank you for banking with us!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        break  # Exit the outer loop after successful login
    
    else:
        print("Invalid PIN.")
        attempt += 1
        if attempt == 3:
            print("Your ATM card is blocked due to 3 incorrect attempts.")
