class User:
    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password

    def turn_into_dict(self):
        user_data = {"name": self.name, "user": self.user_name, "password": self.password}
        return user_data
