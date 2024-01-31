import csv


class AccessControlPolicy:
    def __init__(self, role) -> None:
        self._role = role

    def setRole(self, set_role) -> str:
        self._role = set_role

    def getRole(self) -> str:
        return self._role

    def getPermissions(self) -> dict:
        with open("AccessControlMatrix.csv", "r") as CSVFile:
            CSVReader = csv.DictReader(CSVFile)
            data = [row for row in CSVReader]
            for item in data:
                found_role = item.pop("Role")
                if found_role == self._role:
                    return item
