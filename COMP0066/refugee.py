from human import human

#refugee do not need to log in so it doesnot need

#refugee json 存储格式是, {key:[name, phone, sex, age, status, [refugee_name list], camp_name}
#refugee对象不用包含camp名字，在储存格式中加入camp名字
class refugee(human):
    def __init__(self, name, phone, sex, age, status, families = []):
        super(refugee, self).__init__(2, name, phone, sex, age)
        self.id = "2"+"name"
        self.families = families
        self.healthy_status = status
        self.num_family = len(self.families)

    def getID(self):
        """
        get method of ID
        :return: (string)
        """
        a = self.id
        return a
    def setStatus(self, status):
        """
        set method of self.status
        :param status: refugee health status
        :return: None
        """
        self.healthy_status = status

    def getStatus(self):
        """
        get method of self.status
        :return: (String)
        """
        a = self.healthy_status
        return a

    def add_family(self, refugee_name):
        self.families.append(refugee_name)
        self.num_family += 1

    def getFamilies(self):
        """
        get the information of the
        :return: (list)
        """
        a = self.families
        return a

    def getNumFamily(self):
        """
        get method of family member number
        :return: (int)
        """
        a = self.num_family
        return a




