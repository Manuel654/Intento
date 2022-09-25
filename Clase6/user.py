class User:
    def __init__(self, email, password):
        self.__email = email #se esconde este dato con __
        self.__password = password #se esconde este dato con __
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.email = value
        return self.__email
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value2):
        self.password = value2
        return self.__password

    