"""A simple ATM program to see the balance, last movement of the credit card, to transfer money to another bank
account or to draw/add money. They user can interact with the program by typing the number of choice and doing
his/her job. """

# Import the time library for the sleep method, just for the program to look better
import time


class Program:
    """ Class for personal information of the client"""

    def __init__(self):
        # Info for the credit card, what is the name
        self.cardholder = ()
        # pin of the card
        self.pin = ()
        self.amount = 10000  # display the client's amount if chosen
        self.Bank = [  # list of the most common banks in Greece
            "1: 'Apha Bank'",
            "2: 'Eurobank'",
            "3: 'Pireous Bank'",
            "4: 'National Bank of Greece'",
            "5: 'None of the above'"
        ]
        self.option = [
            "1: 'Check Balance",
            "2: 'Withdraw/Deposit'",
            "3: 'Transfer Money To Another Bank Account'",
            "4: 'Quit"
        ]

    def holder(self):
        """Ask the client for name, father's first name and last name. E.G. Juliano A. Jika"""
        self.cardholder = str(
            input('Insert your first and last name: ')).upper()
        # for a cool effect
        print('Processing...')
        time.sleep(0.8)
        return self.cardholder

    def password(self, tries=5):
        """Ask the client to type the pin of the credit card"""
        passw = input('Type the PIN here(4 Digits only!):  ')
        # If the password is more than 4 numbers, then its wrong
        if not len(passw) == 4:
            # make a loop and add tries for the user, if the client types 5 times wrong the PIN. then exit the code
            while tries > 1 and not len(passw) == 4:
                tries -= 1
                print('Incorrect PIN! Try again')
                passw = input('Type the PIN here(4 Digits only!): ')
                if tries == 0:
                    print('Processing...')
                    time.sleep(0.8)
                    print('INVALID PIN AGAIN! QUITING...')
                    exit()

    def bankChoice(self):
        """ Ask the user to enter the number of the bank is using. If none of the 4 banks are not what the user uses,\n
         it has the chance to enter manually"""
        # print the available banks. The * and sep, are to print the elements of the list on a different line
        print(*self.Bank, sep="\n")
        # create a loop in case the user does not type a number or outside the range
        while True:
            try:
                clientInput = int(input(
                    "Welcome back {}! Which of the banks above are you using? Type 1-5 here: ".format(self.cardholder)))
                if clientInput == 1:
                    # for a cool effect too
                    print('Processing...')
                    time.sleep(0.8)
                    print(f"Bank chosen: '{self.Bank[0]}'")
                    break
                elif clientInput == 2:
                    print('Processing...')
                    time.sleep(0.8)
                    print(f"Bank chosen: '{self.Bank[1]}'")
                    break
                elif clientInput == 3:
                    print('Processing...')
                    time.sleep(0.8)
                    print(f"Bank chosen: '{self.Bank[2]}'")
                    break
                elif clientInput == 4:
                    print('Processing...')
                    time.sleep(0.8)
                    print(f"Bank chosen: '{self.Bank[3]}'")
                    break
                elif clientInput == 5:
                    print('Processing...')
                    time.sleep(0.8)
                    unlistedBank = str(input('Please type the Bank you are using: '))
                    print('Processing...')
                    time.sleep(0.3)
                    print(f'Bank chosen: "{unlistedBank}"')
                    break
                else:
                    print('Processing...')
                    time.sleep(0.3)
                    print('Invalid Input! Try again!')
                    continue
            except ValueError:
                print('Processing...')
                time.sleep(0.5)
                print('Please type only number from 1 to 5!')
                continue

    def choosingOption(self):
        """Options for the client to choose, which one to run"""
        print(*self.option, sep='\n')
        option = int(input('Please select an option: '))
        while True:
            try:
                if option == 1:
                    print('Processing...')
                    time.sleep(0.4)
                    print(f'Your total amount is: {self.amount}')
                    break
                elif option == 2:
                    print('Processing...')
                    time.sleep(0.4)
                    # if the account balance of the client is above 0, can proceed, else not.
                    if self.amount > 0:
                        confirm = str(input('Would you like to withdraw or to deposit: ')).lower()
                        # a while function to check in order for the client to type correct answer
                        while True:
                            if confirm == 'withdraw':
                                amount = float(input('Enter the amount you would like to withdraw: '))
                                # remove the amount the client wants to withdraw for the account balance
                                self.amount -= amount
                                print('Processing...')
                                time.sleep(0.4)
                                # print the new balance the user has
                                print(f'New balance: {self.amount}')
                                return False  # return false in order to break from the while loop
                            elif confirm == "deposit":
                                depositAmount = float(
                                    input('Please enter the amount of money you would like to deposit: '))
                                self.amount += depositAmount
                                print('Processing...')
                                time.sleep(0.4)
                                print(f"New balance: {self.amount}")
                                return False  # return false in order to break from the while loop
                            # if the client types anything invalid, ask if want to try again or not
                            else:
                                print(f"{confirm} is not a valid option, would you like to try again or quit?")
                                progress = str(input('Type y for yes and n for no: ')).lower()
                                if progress == 'y':
                                    confirm = str(input('Would you like to withdraw or to deposit: ')).lower()
                                    if confirm == 'withdraw':
                                        amount = float(input('Enter the amount you would like to withdraw: '))
                                        # remove the amount the client wants to withdraw for the account balance
                                        self.amount -= amount
                                        print('Processing...')
                                        time.sleep(0.4)
                                        # print the new balance the user has
                                        print(f'New balance: {self.amount}')
                                        return False  # return false in order to break from the while loop
                                    elif confirm == "deposit":
                                        depositAmount = float(
                                            input('Please enter the amount of money you would like to deposit: '))
                                        self.amount += depositAmount
                                        print('Processing...')
                                        time.sleep(0.4)
                                        print(f"New balance: {self.amount}")
                                    else:
                                        # if the input still incorrect, exit the program
                                        print('Exiting...')
                                        time.sleep(0.5)  # to make it little dramatic
                                        exit()
                                elif progress == 'n':
                                    return False
                                else:
                                    print('Processing...')
                                    time.sleep(0.4)
                                    print('Invalid input! Try again!')
                                    continue
                elif option == 3:
                    otherBank = str(input('Please enter the number of the bank you would like to transfer money: '))
                    print('Processing...')
                    time.sleep(0.2)
                    amountSending = float(input('Please enter the amount you would like to send: '))
                    # A while loop in case the user types string instead of numbers
                    while True:
                        try:
                            # if the amount is greater than the balance, ask the user to try again until the right amount
                            if amountSending > self.amount:
                                print('Processing...')
                                time.sleep(0.2)
                                print(f'Your balance is: {self.amount}! You can not send {amountSending}!')
                                amountSending = float(input('Please enter the amount you would like to send: '))
                                continue
                            # elif instead of else, due to else will not let the errors run for the except method
                            elif amountSending <= self.amount:
                                break
                        except ValueError:
                            print('Invalid input! Please type only numbers!')
                            continue
                    self.amount -= amountSending  # remove the amount the client sent from the total client's balance
                    print(f'{otherBank} got the {amountSending} you sent!')
                    print(f'Your new balance now is: {self.amount}')  # inform the client for the new balance
                    break
                elif option == 4:
                    """if the client wants to exit the program, then add an exit method"""
                    print('Processing...')
                    time.sleep(0.3)
                    print('Thank you for choosing us!\nHave a nice one!')
                    exit()
            except ValueError:
                print('Invalid input! Try again!')
                continue

    def anythingElse(self):
        """A function to add in the options, in order when the client finishes with something, ask if wants any other transition"""
        confirming = str(input('Would you like anything else or you finished :)(type yes or no): ')).lower()
        # NOTE: even if the client had choose to quit previously, the program will still exit and will not run this function
        if confirming == 'no' or confirming == 'n' or confirming == ' no':
            print('Quiting...')
            time.sleep(0.2)
            quit()
        elif confirming == 'yes' or confirming == 'y' or confirming == 'ye':
            print('Processing...')
            time.sleep(0.3)
            self.choosingOption()
        else:
            print('Processing...')
            time.sleep(0.5)
            print('Invalid Input! Try again!')
            self.anythingElse()


if __name__ == '__main__':
    start = Program()
    start.holder()
    start.password()
    start.bankChoice()
    start.choosingOption()
    start.anythingElse()
