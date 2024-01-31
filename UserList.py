import os

import User
import AccessControlPolicy
import PasswordEncrypter

policy = AccessControlPolicy
encrypter = PasswordEncrypter.PasswordEncrypter()

regularClientRole = policy.AccessControlPolicy("RegularClient")
premiumClientRole = policy.AccessControlPolicy("PremiumClient")
financialAdvisorRole = policy.AccessControlPolicy("FinancialAdvisor")
financialPlannerRole = policy.AccessControlPolicy("FinancialPlanner")
investmentAnalystRole = policy.AccessControlPolicy("InvestmentAnalyst")
complianceOfficerRole = policy.AccessControlPolicy("ComplianceOfficer")
technicalSupportRole = policy.AccessControlPolicy("TechnicalSupport")
tellerRole = policy.AccessControlPolicy("Teller")


def instantiateUsers():
    os.remove("./passwd.txt")
    mischa = User.User("mischa", regularClientRole)
    encrypter.registerAccount("mischa", "RegularClient", "Grapefruit5$")
    veronica = User.User("veronica", regularClientRole)
    encrypter.registerAccount("veronica", "RegularClient", "Grapefruit5$")

    winston = User.User("winston", tellerRole)
    encrypter.registerAccount("winston", "Teller", "Grapefruit5$")
    kelan = User.User("kelan", tellerRole)
    encrypter.registerAccount("kelan", "Teller", "Grapefruit5$")

    nelson = User.User("nelson", financialAdvisorRole)
    encrypter.registerAccount("nelson", "FinancialAdvisor", "Grapefruit5$")
    kelsie = User.User("kelsie", financialAdvisorRole)
    encrypter.registerAccount("kelsie", "FinancialAdvisor", "Grapefruit5$")

    howard = User.User("howard", complianceOfficerRole)
    encrypter.registerAccount("howard", "ComplianceOfficer", "Grapefruit5$")
    stefania = User.User("stefania", complianceOfficerRole)
    encrypter.registerAccount("stefania", "ComplianceOfficer", "Grapefruit5$")

    willow = User.User("willow", premiumClientRole)
    encrypter.registerAccount("willow", "PremiumClient", "Grapefruit5$")
    nala = User.User("nala", premiumClientRole)
    encrypter.registerAccount("nala", "PremiumClient", "Grapefruit5$")

    stacy = User.User("stacy", investmentAnalystRole)
    encrypter.registerAccount("stacy", "InvestmentAnalyst", "Grapefruit5$")
    keikilana = User.User("keikilana", investmentAnalystRole)
    encrypter.registerAccount("keikilana", "InvestmentAnalyst", "Grapefruit5$")

    kodi = User.User("kodi", financialPlannerRole)
    encrypter.registerAccount("kodi", "FinancialPlanner", "Grapefruit5$")
    malikah = User.User("malikah", financialPlannerRole)
    encrypter.registerAccount("malikah", "FinancialPlanner", "Grapefruit5$")

    caroline = User.User("caroline", technicalSupportRole)
    encrypter.registerAccount("caroline", "TechnicalSupport", "Grapefruit5$")
    pawel = User.User("pawel", technicalSupportRole)
    encrypter.registerAccount("pawel", "TechnicalSupport", "Grapefruit5$")

    userList = [mischa, veronica, winston, kelan, nelson, kelsie, howard,
                stefania, willow, nala, stacy, keikilana, kodi, malikah, caroline, pawel]

    return userList


def printPermissions():
    for user in instantiateUsers():
        print(user.getUsername() + "'s permissions: ")
        permissions = user.getPermissions()
        for permission in permissions:
            print(permission + "=" + permissions[permission])
        print("\n")


printPermissions()
