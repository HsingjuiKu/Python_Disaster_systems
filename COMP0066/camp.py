import js as j

# def check_number_refugee():
#     path = "refugee.json"
#     data = j.read(path)["refugee"]
#     camp_name = {}
#     camp_numbner = {}
#     for key in data:
#         if data[key][5] in camp_name:
#             #camp_numbner[data[key][5]] 是名字
#             number = camp_numbner[data[key][5]]
#             camp_numbner[data[key][5]] = number + 1
#         else:
#             camp_name.add(camp_numbner[data[key][5]])
#             camp_numbner[camp_numbner[data[key][5]]] = 1
#
#     return camp_numbner

# camp json 存储格式是, {key:[name, [refugee_name list], have_emergency}
health_weight_water = {"No pain": 5, "Mild pain": 6, "Moderate pain": 8, "Severe pain": 4, "Worst pain/EMERGENCY": 3}
health_weight_food = {"No pain": 8, "Mild pain": 6, "Moderate pain": 4, "Severe pain": 2, "Worst pain/EMERGENCY": 1}
health_weight_medical = {"No pain" : 0, "Mild pain" : 1, "Moderate pain" : 3, "Severe pain" : 5,
                         "Worst pain/EMERGENCY": 10}
# age_weight_water = {"young" : 4, "middle" : 6, "old" : 3}


class camp:
    def __init__(self, name, refugees=[], have_emergency=False):
        """
        Initial function for creating camp
        :param name:
        :param refugees:
        """
        self.name = name
        self.refugees = refugees
        self.num_Refugee = len(self.refugees)
        # 一个营地只能属于一个plan
        self.camp_have_plan = have_emergency



    def compute_water(self):
        refugee_data = j.read("refugee.json")["refugee"]
        water = 100
        for r in self.refugees:
            for i in refugee_data:
                if r == i:
                    health = refugee_data[i][4]
                    water -= health_weight_food[health]
                    # if year <= 20 and year > 0:
                    #     water -= age_weight_water["young"]
                    # elif year > 20 and year <= 60:
                    #     water -= age_weight_water["middle"]
                    # else:
                    #     water -= age_weight_water["old"]
            if water <= 0:
                return 0
        return water


    def compute_food(self):
        refugee_data = j.read("refugee.json")["refugee"]
        food = 100
        for r in self.refugees:
            for i in refugee_data:
                if r == i:
                    health = refugee_data[i][4]
                    food -= health_weight_food[health]
            if food <= 0:
                return 0
        return food


    def compute_medical(self):
        refugee_data = j.read("refugee.json")["refugee"]
        medical = 100
        for r in self.refugees:
            for i in refugee_data:
                if r == i:
                    health = refugee_data[i][4]
                    medical -= health_weight_medical[health]
            if medical <= 0:
                return 0
        return medical


    def check_status(self):
        if self.water == 0 or self.food == 0 or self.medical == 0:
            return False
        else:
            return True

    def getName(self):
        """
        Get Method of self.name
        :return: (String)
        """
        a = self.name
        return a

    def getWater(self):
        return self.water

    def getFood(self):
        return self.food

    def getMedical(self):
        return self.medical

    def getStatus(self):
        return self.status

    def getCamp_have_plan(self):
        return self.camp_have_plan

    def setCamp_have_plan(self, change):
        self.camp_have_plan = change




