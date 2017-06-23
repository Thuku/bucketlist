"""
This class manages users of the bucket list application
"""


class User(object):
    """
    """
    users = []

    def create_user(self, email, password, confirm_password):
        """
        Create a new user in the list
        """
        while len(password) >6 and len(confirm_password)>6:
            if password != confirm_password:
                error = "Password mismatch. Please try again"
                return error
            else:
                user_id = len(self.users)+1
                new_user = {"id": user_id, "email": email, "password": password}

                emails = set((user['email']) for user in self.users)
                if (new_user['email']) not in emails:
                    self.users.append(new_user)
                    msg = ''
                    print(self.users)
                    return msg
                else:
                    error = "User with that email already exists"
                    return error
        else:
            error = "Password length is less than 6 characters"
            return error
        

    def login(self, email, password):
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                return True

            else:
                return False
