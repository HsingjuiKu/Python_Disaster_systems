from human import human
import emergency_plan as e
import js as j
import volunteer as v
import datetime
from camp import camp
class admin(human):
    def __init__(self, name, phone, sex, age, username, password):
        """
        initial method of admin
        :param name: (String)
        :param phone: (int)
        :param sex: (Boolean)
        :param age: (int)
        :param username: (String)
        :param password: (int)
        """
        super(admin, self).__init__(0, name, phone, sex, age, username, password)
        self.id = "0" + self.username

    def getID(self):
        """
        get method of ID
        :return: (String)
        """
        a = self.id
        return a


    def create_Volunteer(self, username, password, name, phone, sex, camp, status):
        path = "volunteer.json"
        volu = v.volunteer(username, password, name, phone, sex, camp, status)
        data = j.read(path)["volunteer"]
        newdata = [username, password, name, phone, sex, camp, status]
        data[username] = newdata
        j.write(path, {"volunteer" : data})
        path = "account.json"
        data = j.read(path)["account"]
        data[username] = password
        j.write(path, {"account" : data})
        return volu

    def stop_Volunteer(self, volunteer):
        """
        stop the volunteer account status
        :param volunteer: (volunteer)
        :return: None
        """
        volunteer.setStatus(False)
        path = "volunteer.json"
        username = volunteer.getUserName()
        data = j.read(path)["volunteer"]
        for key in data:
            if key == username:  # use ==
                data[key][6] = False
        j.write(path, {"volunteer":data})

    def reactive_Volunteer(self, volunteer):
        """
        active the volunteer account status
        :param volunteer: (volunteer)
        :return: None
        """
        path = "volunteer.json"
        volunteer.setStatus(True)
        username = volunteer.getUserName()
        data = j.read(path)["volunteer"]
        for key in data:
            if key == username:
                data[key][6] = True
        j.write(path, {"volunteer":data})


    def delete_Volunteer(self, volunteer):
        """
        delete voluteer account in relevant file
        :param volunteer: (volunteer)
        :return:
        """
        #delete the record of volunteer in json
        path = "volunteer.json"
        data = j.read(path)["volunteer"]
        for key in data:
            if key == volunteer.getUserName():
                del data[key]
                break
        #更新文件
        j.write(path, {"volunteer":data})
        path = "account.json"
        data = j.read(path)["account"]
        for key in data:
            if key == volunteer.getUserName():
                del data[key]
                break
        j.write(path, {"account":data})
        return

    def create_emergency_plan(self, name, kind, description, region, begin_date = datetime.datetime.today(), end_date = datetime.date(2099,1,1), camps=()):
        """
        admin create emergency plan
        :param kind: (String)
        :param description: (String)
        :param region: (String)
        :param begin_date: (Datetime)
        :param end_date: (Datetime)
        :param camps: (list) camp name list
        :return:
        """
        path = "emergency_plan.json"
        plan = e.emergency_plan(name, kind, description, region, begin_date, end_date, camps)
        data = j.read(path)["emergency_plan"]
        newdata = [name, kind, description, region, (begin_date.strftime('%Y'),
                                                     begin_date.strftime('%m'),
                                                     begin_date.strftime('%d')),
                                                    (end_date.strftime('%Y'), end_date.strftime('%m'), end_date.strftime('%d')), camps]
        data[name] = newdata
        j.write(path, {"emergency_plan": data})
        return plan

    def check_emergency(self, emergency):
        """
        get all information of emergency
        :param emergency: (emergency_plan)
        :return: (Dictionary)
        """
        return emergency.showContent()

    def create_camp(self, name):
        data = j.read("camp.json")
        data[name] = name
        j.write("camp.json", {"camp":data})


    def del_plan(self, plan):
        e_data = j.read("emergency_plan.json")["emergency_plan"]
        c_data = j.read("camp.json")["camp"]
        r_data = j.read("refugee.json")["refugee"]
        v_data = j.read("volunteer.json")["volunteer"]

        refugee_list = []
        for e in e_data:
            if e == plan:
                camp_list = e_data[e][6]
                break
        del e_data[plan]

        for v in v_data:
            if v_data[v][5] == plan:
                v_data[v][5] = "No Work"

        for camp in camp_list:
            for c in c_data:
                if camp == c:
                    refugee_list += c_data[c][1]
                    del c_data[camp]
                    break

        for refugee in refugee_list:
            for r in r_data:
                if refugee == r:
                    del r_data[refugee]
                    break

        j.write("emergency_plan.json", {"emergency_plan":e_data})
        j.write("camp.json", {"camp":c_data})
        j.write("refugee.json", {"refugee":r_data})
        j.write("volunteer.json", {"volunteer":v_data})












