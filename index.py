print("Please insert your ATM YES/NO")

# pin chance
chance = 3

# ATM pin
pin = 9511

# balance
balance = 100000

# ATM options
def atm_option():
    print("""   
    1. Check Balance
    2. Withdraw Cash
    3. Deposit Cash
    4. Change Pin
    5. Exit
    """)
    global option  # Declare option as global
    option = int(input("Enter your option: "))
    return option

x = input("Please insert your ATM YES/NO: ").lower()

if x == "yes":
    input_pin = int(input("Enter your pin: "))
    while input_pin != pin:
        if chance == 0:
            print("You have exceeded the number of chances")
            exit()
        print("Incorrect pin")
        chance -= 1
        print("You have " + str(chance) + " chances left")
        input_pin = int(input("Enter your pin: "))
    
    while True:
        atm_option()
        if option == 1:
            print("Your balance is: ", balance)
        elif option == 2:
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Your balance is: ", balance)
            else:
                print("Insufficient funds")
        elif option == 3:
            deposit = int(input("Enter the amount you want to deposit: "))
            balance += deposit
            print("Your balance is: ", balance)
        elif option == 4:
            new_pin = int(input("Enter your new pin: "))
            pin = new_pin
            print("Your pin has been changed successfully")
        elif option == 5:
            print("Thank you for using our ATM")
            break
        else:
            print("Wrong selection")
        
        another_transaction = input("Do you want to perform another transaction YES/NO: ").lower()
        if another_transaction != "yes":
            print("Thank you for using our ATM")
            break
else:
    print("Thank you for using our ATM")
