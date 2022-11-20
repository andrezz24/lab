class Account:
    """
    A class to represent an account object.
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of account object.
        param name: Account name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> float:
        """
        Method that allows the user to deposit into their account balance.
        param amount: Numeric (float) value.
        :return: True or False depending on what user deposits.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> float:
        """
        Method that allows the user to withdraw from their account balance.
        param amount: Numeric (float) value.
        :return:
        """
        if (amount > self.__account_balance) or (amount <= 0):
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method that gets the current account balance.
        :return: Account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method that gets the account name.
        :return: Account name.
        """
        return self.__account_name
