import datetime
import camp
import js as j
#这里我觉得live不要了吧，我看过文件，文件没有写live的存储，我们只需要用存储文件中的两个日期检查是否还可用，将日期按照格式化引入到datetime
class emergency_plan:
    def __init__(self, name, kind, description, region, begin_date, end_date, camps):
        """
        initial function for emergency_plan
        :param kind: (String)
        :param description: (String)
        :param region: (String)
        :param live: (Boolean)
        :param begin_date:
        :param end_date:
        :param camps: (list) camps name
        """
        self.name = name
        self.kind = kind
        self.description = description
        self.region = region
        self.begin_date = begin_date
        self.end_date = end_date
        self.camps = camps
        # self.live = live
    def showContent(self):
        """
        get all information of emergency plan
        :return: (Dictionary
        """
        content = {}
        total = 0
        content['kind'] = self.kind
        content['description'] = self.description
        content['region'] = self.region
        camp_content = []
        for c in self.camps:
            total += c.getnum_Refugee()
            name = c.getName()
            num_volu = c.getnum_Voluneer()
            camp_content.append((name, num_volu))
        content['camp_content'] = camp_content
        content['num_refugee'] = total
        return content

    def addCamp(self, camp):
        """
        add camp of emergency_plan
        :param camp: (camp)
        :return:
        """
        if camp not in self.camps:
            self.camps.append(camp)

    def check_valid(self):
        """
        check the valid of emergency plan
        :return:
        """
        if (self.end_date - self.begin_date) == 0:
            self.live = False


    def find_best_choice_camp(self, refugee_name, health_status):
        """
        Algorithm to find suitable camp
        :param refugee_name: (String)
        :return: (String) camp name
        """
        #增加算法优先性，如果营地中有他的家人，把他和他家人放在一起
        refugee_data = j.read("refugee.json")["refugee"]
        for r in refugee_data:
            for f in refugee_data[r][5]:
                if f == refugee_name:
                    return refugee_data[r][6]


        #如果没有找到他的家人，利用权重寻找优先级
        health_weight = {"No pain": [0.7,0.3,0], "Mild pain": [0.5, 0.3, 0.2], "Moderate pain": [0.4, 0.2, 0.4], "Severe pain": [0.2, 0.4, 0.4],
                        "Worst pain/EMERGENCY": [0.1, 0.4, 0.5]}
        camp_data = j.read("camp.json")["camp"]
        refugee_data = j.read("refugee.json")["refugee"]
        weight_food = health_weight[health_status][0]
        weight_water = health_weight[health_status][1]
        weight_health = health_weight[health_status][2]
        maxmark = 0
        #字符串name
        maxcamp = self.camps[0]
        for c in self.camps:
            for i in camp_data:
                if i == c:
                    camp1 = camp.camp(camp_data[i][0], camp_data[i][1], camp_data[i][2])
                    tempmark = camp1.compute_food() * weight_food + camp1.compute_water() * weight_water + camp1.compute_medical() * weight_health
                    if tempmark > maxmark:
                        maxmark = tempmark
                        maxcamp = c
        return maxcamp