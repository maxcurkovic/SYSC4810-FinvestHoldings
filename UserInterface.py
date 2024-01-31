import getpass
import PasswordChecker
import PasswordEncrypter
import AccessControlPolicy
import User

passwordManager = PasswordEncrypter.PasswordEncrypter()
check = PasswordChecker

listRoles = ["RegularClient", "Teller", "FinancialAdvisor", "ComplianceOfficer", "PremiumClient", "InvestmentAnalyst", "FinancialPlanner",
             "TechnicalSupport"]


def userInterface() -> None:
    print("\nFinvest Holdings: Client Records System")
    registerOrLogin = input("Enter L to login, or R to register a new account: ")
    if registerOrLogin == "L" or registerOrLogin == "l":
        print("Entering login... ")
        loginUI()
    elif registerOrLogin == "R" or registerOrLogin == "r":
        print("Entering register... ")
        registerUI()
    else:
        print("Invalid command. Type L or R. Please try again")
        userInterface()

def registerUI():
    print("\nFinvest Holdings: Client Records System")
    print("Register User")
    print("First, enter a valid role. List of valid roles include: ")
    for item in listRoles:
        print(item)
    role = input("Role: ")
    if role not in listRoles:
        print("Account creation unsuccessful. Role not valid.")
        registerUI()
    print("Next, enter a username and password.")
    username = input("Username: ")
    if passwordManager.checkExistingUsername(username):
        print("Account creation unsuccessful. You are trying to enter a username that already exists. ")
        registerUI()
    password = getpass.getpass(prompt="Enter password: ")
    if check.checkIfUsername(username, password) == False and check.checkLicensePlate(
            password) == False and check.checkCalendarDateOrPhoneNumber(password) == False and check.checkIfWeak(password) == False and check.checkCharacters(
            password) == True and check.checkPasswordLength(password) == True:
        passwordManager.registerAccount(username, role, password)
        print("Account successfully created!")
        userInterface()
    else:
        print("Account creation unsuccessful. Your password must adhere to the following criteria: ")
        print("   - 8 to 12 characters in length")
        print(
            "   - Include one upper-case letter, one lower-case letter, number and special character from {!, @, #, $,"
            "%, ?, *")
        print("   - Not be a weak password as determined by a list of common passwords")
        print("   - Not be a calendar date, license plate number, telephone number, or other common number")
        print("   - Not match your username")
        registerUI()

def loginUI():
    print("\nFinvest Holdings: Client Records System")
    print("Login User")
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")
    print(password)
    (isLoggedIn, role) = passwordManager.loginAccount(username, password)
    userRole = AccessControlPolicy.AccessControlPolicy(role)
    newUser = User.User(username, userRole)
    if isLoggedIn:
        print("\nAccess Granted. Login successful\n")
        print("Username: " + username)
        print("Role: " + role)
        print("Permissions: ")
        userPermissions = newUser.getPermissions()
        for permission in userPermissions:
            print(permission + "=" + userPermissions[permission])
        print("\n")
        command = input("Type L to logout, any other key to quit program: ")
        if command == "L" or "l":
            userInterface()
        else:
            exit()
    else:
        print("Login failed. Your username or password is incorrect. Please try again")
        loginUI()

def main():
    userInterface()

main()
