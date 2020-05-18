class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def is_corrupted(self):
        if len(dir(self)) % 2 == 0:
            return True
        if any([att.startswith('b') for att in dir(self)]):
            return True
        if not (hasattr(self, "addr") or hasattr(self, "zip")):
            return True
        if not hasattr(self, "name") or not hasattr(self, "id") or not hasattr(self, "value"):
            return True
        return False


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def get_account_by_name(self, name):
        for account in self.account:
            if account.name == name:
                return account
        return None

    def get_account_by_id(self, idx):
        if idx >= len(self.account) or idx < 0:
            return None
        return self.account[idx]

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if isinstance(origin, int):
            origin = self.get_account_by_id(origin)
        elif isinstance(origin, str):
            origin = self.get_account_by_name(origin)

        if isinstance(dest, int):
            dest = self.get_account_by_id(dest)
        elif isinstance(dest, str):
            dest = self.get_account_by_name(dest)

        if not isinstance(origin, Account) or not isinstance(dest, Account) or not isinstance(amount, float):
            return False
        if origin.is_corrupted() or dest.is_corrupted():
            return False
        if amount < 0 or amount > origin.value:
            return False
        origin.transfer(-amount)
        dest.transfer(amount)
        return True

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        if isinstance(account, int):
            account = self.get_account_by_id(account)
        elif isinstance(account, str):
            account = self.get_account_by_name(account)
        if not isinstance(account, Account):
            return False

        if not account.is_corrupted():
            return True

        try:
            for att in dir(account):
                if att.startswith('b'):
                    delattr(account, att)
            if not (hasattr(account, "addr") or hasattr(account, "zip")):
                setattr(account, "addr", input("Input Your address:\n>> "))
            if not hasattr(account, "name"):
                setattr(account, "name", input("Input Your Name:\n>> "))
            if not hasattr(account, "id"):
                setattr(account, "id", self.account.index(account))
            if not hasattr(account, "value"):
                setattr(account, "value", 0)
            if len(dir(account)) % 2 == 0:
                setattr(account, "fixed", True)
            return True
        except:
            return False


