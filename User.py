from AccessControlPolicy import AccessControlPolicy


class User:
    def __init__(self, username, role):
        self.__username = username
        self.__role = role

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username) -> None:
        self.__username = username

    def getRole(self) -> AccessControlPolicy:
        return self.__role.getRole()

    def getPermissions(self) -> dict:
        return self.__role.getPermissions()
