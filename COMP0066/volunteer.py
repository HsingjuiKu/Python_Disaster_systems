import emergency_plan
from refugee import refugee
from human import human
import js as j
class volunteer(human):
    def __init__(self, username, password, name, phone, sex, emergency_plan, status = True):
        """
        initial function for class volunteer and inherient human class
        :param username: (string) Log in username
        :param password: (int) Log in password
        :param name: (String) People Name
        :param phone: (int) People's Phone Number
        :param camp: (String) Belong which camp's name
        :param status: (Boolean) True mean valid, False mean invalid
        """
        super(volunteer, self).__init__(1, name= name, phone= phone, sex= sex, username= username, password=password)
        self.emergency_plan = emergency_plan
        self.status = status
        self.id = "1" + self.username
    def setStatus(self, status):
        """
        set method for status
        :param status: (string)
        :return: None
        """
        self.status = status

    def getStatus(self):
        """
        get method for status
        :return: (string)
        """
        a = self.status
        return a
    #Function to create refugee
    def create_refugee_profile(self, name, phone, sex, age, health_status, families):
        """
        Volunteer create new refugee profile, and save the refugee information in file
        :param name: (string) refugee name
        :param phone: (int) refugee phone number
        :param sex: (Boolean) refugee sex
        :param age: (int) refugee age
        :param health_status: (Boolean) refugee health_status
        :return: (refugee)
        """
        emergency_plan_data = j.read("emergency_plan.json")["emergency_plan"]
        camp_data = j.read("camp.json")["camp"]
        for e in emergency_plan_data:
            if self.emergency_plan == e:
                emergency = emergency_plan.emergency_plan(emergency_plan_data[e][0],
                                                          emergency_plan_data[e][1],
                                                          emergency_plan_data[e][2],
                                                          emergency_plan_data[e][3],
                                                          emergency_plan_data[e][4],
                                                          emergency_plan_data[e][5],
                                                          emergency_plan_data[e][6])
        path = "refugee.json"
        r = refugee(name, phone, sex, age, health_status, families)
        choose_camp = emergency.find_best_choice_camp(name, health_status)
        newdata = [name, phone, sex, age, health_status, families, choose_camp]
        info = j.read(path)
        data = info["refugee"] #这里是字典类型
        data[name] = newdata
        j.write(path, {"refugee" : data})

        for c in camp_data:
            if c == choose_camp:
                camp_data[c][1].append(name)
        j.write("camp.json", {"camp" : camp_data})
        return r







