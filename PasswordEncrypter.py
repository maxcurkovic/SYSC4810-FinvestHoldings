import hashlib
import random
class PasswordEncrypter:
    def __init__(self) -> None:
        self.__passwordFile = "./passwd.txt"

    def checkExistingUsername(self, username):
        file = open(self.__passwordFile, "r")
        for account in file:
            account = account.split(" ")
            if account[0] == username:
                file.close()
                return True
        file.close()
        return False

    def registerAccount(self, username, role, password):
        file = open(self.__passwordFile, "a")
        salt = str(random.getrandbits(32))
        password += salt
        passwordHash = hashlib.sha256(password.encode())
        file.write(username + " " + role + " " + salt + " " + passwordHash.hexdigest() + "\n")
        file.close()
        return

    def loginAccount(self, username, password) -> (bool,str):
        file = open(self.__passwordFile, "r")
        for user in file:
            user = user.split(" ")
            user[3] = user[3].replace("\n", "")
            if user[0] == username:
                password = password + user[2]
                passwordHash = hashlib.sha256(password.encode())
                if passwordHash.hexdigest() == user[3]:
                    file.close()
                    return True, user[1]
        file.close()
        return False, None


