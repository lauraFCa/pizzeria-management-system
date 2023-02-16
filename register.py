from connection import Connection


class Register:
    def __init__(self):
        self.__name, self.__password, self.__level = '', '', 1

    ### GETs e SETs ###
    @property  # GET
    def name(self):
        return self.__name

    @name.setter  # SET
    def name(self, name):
        self.__name = name

    @property  # GET
    def password(self):
        return self.__password

    @password.setter  # SET
    def password(self, password):
        self.__password = password

    @property  # GET
    def level(self):
        return self.__level

    @level.setter  # SET
    def level(self, level):
        self.__level = level


    ### Methods ###
    def loginRegister(self, decision, result):
        '''Manage new users login and register

        Returns:
            [bool, bool]: authenticated, masterUser
        '''

        existentUser = False
        authenticated = False
        masterUser = False

        # global decision = xxx --> create a variable to the whole app
        if decision == 1:  # LOGIN (check if user already exists)
            self.__name = input("Type in the Username: ")
            self.__password = input("Type in the Password: ")

            for line in result:
                if self.__name == line['name'] and self.__password == line['password']:
                    if line['level'] == 1:
                        masterUser = False
                    elif line['level'] == 2:
                        masterUser = True
                    authenticated = True
                    break  # stop executing as soon as it finds an equal password
                else:
                    authenticated = False

            if not authenticated:
                print("Wrong user or password")

        elif decision == 2:
            print("\nRegister (Sign Up)!")
            self.__name = input("Type in a Username: ")
            self.__password = input("Type in a Password: ")

            for line in result:
                if self.__name == line['name'] and self.__password == line['password']:
                    existentUser = True

            if existentUser:
                print(
                    'User and password already registered!\nTry a different name or password\n')

            elif existentUser == False:
                query = 'INSERT INTO users(name, password, level) VALUES ("{}", "{}", {})'.format(
                    self.__name, self.__password, 1)
                Connection().commitBD(query, 'User successfully registered!',
                                   'Error inserting user on system!')

        return authenticated, masterUser
