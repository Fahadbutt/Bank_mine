__author__ = 'fahad'
# BANK code by FAHAD MASOOD BUTT
# Defining Class Member of the BANK with 
# :Account Name,Bank Account ID,Bank balance,
# password of online Account, Bank Account Type
class Member(object):
    """ class defined """
    def __init__(self, name, bank_id, balance, password, type):
        self.Name = name
        self.BankID = bank_id
        self.balance = balance
        self.Password = password
        self.type = type

# OVERLOADING Operators for this CLASS Member
    def __lt__(self, other):
        """ operator '<' """
        print"****** OPERATOR ' < ' OVERLOADED ******"
        name = self.Name
        if self.balance < other.balance:
            print"%r has Lesser balance as compared to %r"\
                 % (name, other.Name)
        else:
            print " %r has Greater or Equal balance as " \
                  "compared to %r" % (name, other.Name)
        return self.balance < other.balance

    def __gt__(self, other):
        """ operator '>' """
        print"****** OPERATOR ' > ' OVERLOADED ******"
        name = self.Name
        if self.balance > other.balance:
            print"%r has Greater balance as compared " \
                 "to %r" % (name, other.Name)
        else:
            print " %r has Lesser or Equal balance as " \
                  "compared to %r" % (name, other.Name)
        return self.balance > other.balance

    def __le__(self, other):
        """ operator '<=' """
        print"****** OPERATOR ' <= ' OVERLOADED ******"
        name = self.Name
        if self.balance <= other.balance:
            print"%r has Lesser or Equal balance as " \
                 "compared to %r" % (name, other.Name)
        else:
            print " %r has Greater balance as " \
                  "compared to %r" % (name, other.Name)
        return self.balance <= other.balance

    def __ge__(self, other):
        """ operator '>=' """
        print"****** OPERATOR ' >= ' OVERLOADED ******"
        name = self.Name
        if self.balance >= other.balance:
            print"%r has Greater or Equal balance " \
                 "as compared to %r" % (name, other.Name)
        else:
            print " %r has Lesser balance as " \
                  "compared to %r" % (name, other.Name)
        return self.balance >= other.balance

    def __ne__(self, other):
        """ operator '!=' """
        print "****** OPERATOR ' != ' OVERLOADED ******"
        name = self.Name
        if self.balance != other.balance:
            print"%r has Different balance as " \
                 "compared to %r" % (name, other.Name)
        else:
            print " %r has Lesser/Greater balance " \
                  "as compared to %r" % (name, other.Name)
        return self.balance != other.balance

# Bank Number:shows how many Users Bank has,
# It is used as Bank ID and It is Auto
# generated for a NEW USER
ID = 000000000
ID += 1
# Array to Store Members Initialized by inserting some members
MEMBER_ONE = Member("Fahad butt", ID, 20000, "EE", "savings")
ID += 1
MEMBER_TWO = Member("Shahzad shameer", ID, 25000, "CS", "current")
ID += 1
MEMBER_THREE = Member("Irtaza", ID, 25000, "CS1", "current")

MY_MEMBER = [MEMBER_ONE, MEMBER_TWO, MEMBER_THREE]

# this function just Displays the Bank
# Balance of a Login Account
def check_balance(name, bank_id, password):
    """ function for balance check """
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and\
                        MY_MEMBER[i].Password == password and \
                        MY_MEMBER[i].BankID == bank_id:
            balance = MY_MEMBER[i].balance
            print "****************************************"
            print "**********Account Balance : %r *********" % balance
            print "****************************************"
    what_to_do(name, bank_id, password)

# This Function is for withdrawing some money
# from a Login Account you just have to Enter Amount
def draw_money(name, bank_id, password):
    """ function for money draw """
    amount = int(raw_input("Enter Amount to withdraw:"))
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and \
                        MY_MEMBER[i].Password == password and \
                        MY_MEMBER[i].BankID == bank_id:
            if MY_MEMBER[i].balance >= amount:
                MY_MEMBER[i].balance -= amount
                new_balance = MY_MEMBER[i].balance
                print"*************************"
                print"****Withdrawing Cash*****"
                print"your New Bank balance: %r" % new_balance
                print"Amount Withdraw: %r" % amount
                print"*************************"

            else:
                print"your Account Balance is low!! "
                print"Transaction Failed..."
                what_to_do(name, bank_id, password)
                return
    what_to_do(name, bank_id, password)

# This Function is for Depositing some money
#  from a Login Account you just have to Enter Amount
def cash_deposit(name, bank_id, password):
    """ function for cash deposit """
    amount = int(raw_input("Enter Amount to Deposit:"))
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and \
                        MY_MEMBER[i].Password == password and \
                        MY_MEMBER[i].BankID == bank_id:
            old_balance = MY_MEMBER[i].balance
            MY_MEMBER[i].balance += amount
            new_balance = MY_MEMBER[i].balance
            print"*************************"
            print"****Depositing Cash******"
            print"your Old Bank balance: %r" % old_balance
            print"Amount Deposited: %r" % amount
            print"your New Bank balance: %r" % new_balance
            print"*************************"
    what_to_do(name, bank_id, password)

# This Function is for Paying some BILLS from a
# Login Account you just have to Enter Amount
def deposit_bills(name, bank_id, password):
    amount = int(raw_input("Enter bill balance:"))
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and \
                        MY_MEMBER[i].Password == password and \
                        MY_MEMBER[i].BankID == bank_id:
            if MY_MEMBER[i].balance >= amount:
                MY_MEMBER[i].balance -= amount
                new_balance = MY_MEMBER[i].balance
                print"*************************"
                print"****** Paying bills *****"
                print"your New Bank balance: %r" % new_balance
                print"Amount Deducted: %r" % amount
                print"Bill Paid !!"
                print"*************************"
            else:
                print"your Account Balance is low!! "
                print"Bill payment Failed..."
                what_to_do(name, bank_id, password)
                return
    what_to_do(name, bank_id, password)

# This Function is for Transferring some money
# from a Login Account you just have to Enter
#  other Account details
def transfer_money(name, bank_id, password):
    amount = int(raw_input("Amount to be transferred:"))
    print"Enter Account data to transfer Money:"
    name_other = raw_input("Account Name:")
    bank_id_other = int(raw_input("Bank ID:"))
    for i in range(0, len(MY_MEMBER)):
        # check to see if the other Account
        # details you Entered is Authentic or NOT
        if MY_MEMBER[i].Name == name_other \
                and MY_MEMBER[i].BankID == bank_id_other:
            transfer(name, bank_id, password,
                     name_other, bank_id_other, amount)
    print "ERROR: This Account in which you" \
          " want to Transfer doesn't Exist"
    print "Account name: %r and " \
          "Bank ID: %09d" % (name_other, bank_id_other, )
    print "Do it Again"
    transfer_money(name, bank_id, password)

# This function does the money
# transfer if everything is OK!!
def transfer(name, bank_id, password,
             name_other, bank_id_other, amount):
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and \
                        MY_MEMBER[i].BankID == bank_id and \
                        MY_MEMBER[i].Password == password:
            MY_MEMBER[i].balance -= amount
            balance2 = MY_MEMBER[i].balance
            print"*********** your new balance: " \
                 "%r *************" % balance2
        if MY_MEMBER[i].Name == name_other and \
                        MY_MEMBER[i].BankID == bank_id_other:
            MY_MEMBER[i].balance += amount
            balance1 = MY_MEMBER[i].balance
            print"*******************************" \
                 "***********************"
            print"******************* Transfer Done !! " \
                 "*****************"
            print"*********Amount transferred: %r " \
                 "**********************" % amount
            print"%r New Balance: %r of Bank ID: " \
                 "%09d" % (name_other, balance1, bank_id_other, )
            print"*********************************" \
                 "*********************"
    what_to_do(name, bank_id, password)


# This Function is for Displaying
# Account Type from a Login Account
def check_account_type(name, bank_id, password):
    """Function for Account type check """
    print"****************************************"
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and \
                        MY_MEMBER[i].BankID == bank_id and \
                        MY_MEMBER[i].Password == password:
            type_entered = MY_MEMBER[i].type
            print"WELL!! Your Account Type is:: %r" % type_entered
            print"****************************************"
    what_to_do(name, bank_id, password)

# This Function is for Comparing Accounts from
# a Login Account you just have to Enter Other Account Details
def compare_accounts(name, bank_id, password):
    """compare Accounts """
    print"Add other Account Detail for Comparison"
    name_other = raw_input("Account Name: ")
    bank_id_other = int(raw_input("Bank ID: "))
    for i in range(0, len(MY_MEMBER)):
        # check to see if the other Account details you Entered is Authentic or NOT
        if MY_MEMBER[i].Name == name_other and MY_MEMBER[i].BankID == bank_id_other:
            compare(name, bank_id, password, name_other, bank_id_other)
            return
    print"ERROR: This Account for Comparison doesn't Exist!"
    print "Account name: %r and Bank ID: %09d" % (name_other, bank_id_other, )
    print "Do it Again"
    compare_accounts(name, bank_id, password)

# This function Does the comparison of Accounts
# if your Details entered of other Account are Valid
def compare(name, bank_id, password, name_other, bank_id_other):
    """compare Accounts if All info is Valid """
    print"****** Lets Do Accounts Comparison ********"
    balance1 = 0
    balance2 = 0
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name and \
                        MY_MEMBER[i].BankID == bank_id and \
                        MY_MEMBER[i].Password == password:
            balance1 = MY_MEMBER[i].balance
            
        if MY_MEMBER[i].Name == name_other and \
                        MY_MEMBER[i].BankID == bank_id_other:
            balance2 = MY_MEMBER[i].balance
    if balance1 > balance2:
        # Comparison1: if Greater Amount in Bank balance
        print"***************************************"
        print"*********** HURRAY!! ******************"
        print" Your balance is Greater than %r " % name_other
        print"Yours balance: %r \n %r " \
             "balance: %r " % (balance1, name_other, balance2)

    elif balance1 == balance2:
        # Comparison2: if EQUAL Amount in Bank balance
        print"***************************************"
        print"************* WELL!! ******************"
        print" Balance in both Accounts are Equal "
        print"Yours balance: %r \n %r " \
             "balance: %r " % (balance1, name_other, balance2)

    elif balance1 < balance2: # Comparison3: if Lesser Amount in Bank balance
        print"***************************************"
        print"*********** OOPS!! ********************"
        print" Your balance is Less than %r " % name_other
        print"Yours balance: %r \n %r " \
             "balance: %r " % (balance1, name_other, balance2)

    what_to_do(name, bank_id, password)



# This Function just create a Account
def account_create():
    """create account"""
    print" "
    print"Please Add Details of your Account"
    name = raw_input("User name:")
    for i in range(0, len(MY_MEMBER)):
        if MY_MEMBER[i].Name == name:
            # Check for Account name if it already
            # exist AS ACCOUNT NAME IS UNIQUE
            print"Name %r Already Exist" % name
            print"try some combinations"
            print"Its in Bank Policy to Have a unique Account Name"
            print"*********** PLEASE COOPERATE  ***************"
            account_create()
            return

        else:
            print" Account Name OK!!"
            break
    password = raw_input('password:')
    type_entered = raw_input("Enter Account Type: savings OR current?")
    # only two options for Account type others are INVALID
    if type_entered == "savings":
        print"Account Created"
    elif type_entered == "current":
        print"Account Created"
    else:
        print"Add Correct Account type"
        print"Account not created"
        account_create()
    identity = ID + 1
    member_new = Member(name, identity, 0, password, type_entered)
    MY_MEMBER.append(member_new)
    print"Your Account has been created"
    print"Account Name:%r" % name
    print"Bank Account ID:%09d" % (id,)

# This function is called is user wants to
# login he/she just has to Enter all details
# ACCOUNT NAME & PASSWORD & BANK ID
def login_account():
    """login into account"""
    print " "
    print"Login into Your Account"
    name = raw_input("User Name:")
    bank_id = int(raw_input("Bank Account ID - 9 Digits:"))
    password = raw_input("password:")

    for i in range(0, len(MY_MEMBER)):
        if (MY_MEMBER[i].Name == name) \
                & (MY_MEMBER[i].Password == password) &\
                (MY_MEMBER[i].BankID == bank_id):
            print"Login Successfully As Username: %r" % name
            what_to_do(name, bank_id, password)
            return
    print 'ERROR:Login Failed!!'


# this function just give member options to DO OPERATIONS
def what_to_do(name, bank_id, password):
    print"**************************************************"
    print"Choose what to do:"
    print "1: Check Balance \n2: Draw Money \n3: Deposit bills"
    print "4: Transfer Money \n5: Check Account Type"
    print "6: Compare Accounts \n7: Cash Deposit \n8: logout"

    options = int(raw_input("Select:"))
    if options == 1:
        check_balance(name, bank_id, password)
    elif options == 2:
        draw_money(name, bank_id, password)
    elif options == 3:
        deposit_bills(name, bank_id, password)
    elif options == 4:
        transfer_money(name, bank_id, password)
    elif options == 5:
        check_account_type(name, bank_id, password)
    elif options == 6:
        compare_accounts(name, bank_id, password)
    elif options == 7:
        cash_deposit(name, bank_id, password)
    elif options == 8:
        print " logging Out........"
    else:
        print"ERROR: Please Select given options"
        what_to_do(name, bank_id, password)

# MY MAIN BANK FUNCTION
def main_func():
    """main function"""
    print "******************************************" \
          "***********************************"
    print '*******************  WELCOME TO THE BANK ***' \
          '*********************************'
    print "************************************************" \
          "*****************************"
    print" "
    print " "

    print "Choose your Option:"
    print "1: Create a New Account"
    print "2: Login into Your Account"

    option = int(raw_input("Select:"))
    if option == 1:
        account_create()

    elif option == 2:
        login_account()
    else:
        print"ERROR: Choose Correct option"

# this function just checks for the Operators
#  that are overloaded for MEMBER class
def my_stuff():
    result1 = MEMBER_ONE > MEMBER_TWO
    print" Result1: %r \n\n" % result1

    result2 = MEMBER_ONE < MEMBER_TWO
    print" Result2: %r\n\n" % result2

    result3 = MEMBER_ONE != MEMBER_THREE
    print" Result3: %r\n\n" % result3

    result4 = MEMBER_ONE >= MEMBER_TWO
    print" Result4: %r\n\n" % result4

    result5 = MEMBER_ONE <= MEMBER_TWO
    print" Result5: %r\n\n" % result5

my_stuff()

while 1:
    main_func()
