def checkPasswordLength(password) -> bool:
    counter = 0
    for char in password:
        counter += 1
    if counter < 8:
        print("Password validation failed: Password is not at least 8 characters long!")
        return False
    return True


def checkCharacters(password) -> bool:
    containsUpper = False
    containsLower = False
    containsNumber = False
    containsSpecial = False
    specialCharacters = ["!", "@", "#", "$", "%", "?", "*"]
    for char in password:
        if char.isupper():
            containsUpper = True
        elif char.islower():
            containsLower = True
        elif char.isnumeric():
            containsNumber = True
        elif char in specialCharacters:
            containsSpecial = True
    if containsNumber and containsUpper and containsLower and containsSpecial:
        return True
    print("Password validation failed: Does not contain either an upper case, lower case, number, or special character!")
    return False


# For this one, using the passwords from the following website: https://www.beckershospitalreview.com/cybersecurity/30-most-common-passwords-of-2023.html
def checkIfWeak(password) -> bool:
    weakPasswordList = ["123456", "password", "123456789", "12345", "12345678", "qwerty", "1234567", "111111",
                        "1234567890", "123123", "abc123", "1234", "password1", "iloveyou", "1q2w3e4r", "000000",
                        "qwerty123", "zaq12wsx", "dragon", "sunshine", "princess", "letmein", "654321", "monkey",
                        "27653", "1qaz2wsx", "123321", "qwertyuiop", "superman", "asdfghjkl"]
    if password in weakPasswordList:
        print("Password validation failed: password is considered a common and weak password!")
        return True
    return False


def checkIfUsername(username, password):
    if username == password:
        print("Password validation failed: password is your username!")
        return True
    return False


# Check for a calendar date (8 digits) or phone number (9 digits), found anywhere within the password
def checkCalendarDateOrPhoneNumber(password) -> bool:
    counter = 0
    curr = 0
    prev = 0
    for char in password:
        if char.isnumeric():
            counter += 1
        elif password[curr].isnumeric() and password[prev].isnumeric() and counter > 0:
            counter += 1
        elif counter != 6:
            counter = 0
        if counter >= 6:
            print("Password validation failed: Password may be a calendar date or phone number!")
            return True
        curr += 1
        prev = curr - 1
    return False


# Check if a license plate - we are assuming Ontario format. This function tests for 7 characters - 4 letters, 3 numbers in order
def checkLicensePlate(password) -> bool:
    if len(password) >= 7:
        if password[0].isalpha() and password[1].isalpha() and password[2].isalpha() and password[3].isalpha():
            if password[4].isdigit() and password[5].isdigit() and password[6].isdigit():
                print("Password validation failed: Password may be a license plate value!")
                return True
    return False
