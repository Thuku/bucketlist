"""
This class manages users of the bucket list application
"""


class Accounts(object):
    """
    """

    def __init__(self):
        self.users = []

    def create_user(self, email, password,confirm_password):
        """
        Create a new user in the list
        """
        if password != confirm_password:
            msg = "Password mismatch. Please try again"
            return msg
        else:
            user = {email: password}
            self.users.append(user)
        print(self.users)

    def login(self, email, password):
        for user in self.users:
            if email in user.keys() and user[email] == password:
                msg = "Welcome to your dashboard"
                print(msg)
                return msg

            else:
                msg = "Failure"
                print(msg)
                return msg
