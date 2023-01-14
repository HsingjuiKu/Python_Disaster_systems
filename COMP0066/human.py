class human:
    def __init__(self, rolenumber, name = None, phone = None, sex = None, age = None, username = None, password = None):
        """
        Initial function for class
        :param rolenumber: (int) Distinguish between administrators-0, volunteers-1, and refugees-2
        :param name: (string) people name
        :param phone: (int) people phone number
        :param sex: (boolean) people sex, Male for True, Female for False
        :param age: (int) people age
        :param username: (string) account username
        :param password: (int) account password
        """
        self.rolenumber = rolenumber
        self.name = name
        self.phone = phone
        self.sex = sex
        self.age = age
        self.username = username
        self.password = password

    def setUserName(self, username):
        '''
        set method for username
        :param username:
        :return: None
        '''
        self.username = username
    def getUserName(self):
        '''
        get method for username
        :return: string
        '''
        a = self.username
        return a

    def setPassword(self, password):
        '''
        set method for password
        :param password:
        :return: None
        '''
        self.password = password

    def getPassWord(self):
        '''
        get method for password
        :return: int
        '''
        a = self.password
        return a
    def setRoleNumber(self, rolenumber):
        '''
        set method for role number
        :param rolenumber:
        :return: None
        '''
        self.rolenumber = rolenumber
    def getRoleNumber(self):
        a = self.rolenumber
        return a
    def setName(self, name):
        self.name = name
    def getName(self):
        a = self.name
        return a
    def setPhone(self, phone):
        self.phone = phone
    def getPhone(self):
        a = self.phone
        return a
    def setSex(self, sex):
        self.sex = sex
    def getSex(self):
        a = self.sex
        return a
    def setAge(self, age):
        self.age = age
    def getAge(self):
        a = self.age
        return a
