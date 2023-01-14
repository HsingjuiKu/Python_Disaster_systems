import js as j
import volunteer as v
import pandas as pd
import camp


def get_information(path):
    name = path[:-5:]
    data = j.read(path)[name]
    list = []
    for key in data:
        list.append(key)
    return list


if __name__ == "__main__":
    print(get_information('volunteer.json'))


def get_information_profile(name):
    data = j.read('emergency_plan.json')['emergency_plan'][name]

    data_camp=[]
    data_vltr=[]

    v_data = j.read('volunteer.json')['volunteer']

    for i in data[6]:
        data_camp.append(j.read('camp.json')['camp'][i][1])

    for i in v_data:
        if v_data[i][5] == name:
            data_vltr.append(i[5])

    print(f'\033[0;34mPlan name\033[0m:         {data[1]}\n'
          f'\033[0;34mDescription\033[0m:       {data[2]}\n'
          f'\033[0;34mRegion\033[0m:            {data[3]}\n'
          f'\033[0;34mStart date\033[0m:        {data[4][0]}-{data[4][1]}-{data[4][2]}\n'
          f'\033[0;34mEnd date\033[0m:          {data[5][0]}-{data[5][1]}-{data[5][2]}\n'
          f'\033[0;34mCamp ID\033[0m:           {" , ".join(data[6])}\n'
          f'\033[0;34mNo. of refugee\033[0m:    {len(data_camp)}\n'
          f'\033[0;34mNo. of volunteer\033[0m:  {len(data_vltr)}')


def get_information_login(path):
    name = path[:-5:]
    data = j.read(path)[name]
    return data


def get_information_profile_volunteer(name):
    data = j.read('volunteer.json')['volunteer'][name]
    print(f'\033[0;34mUsername\033[0m:   {data[0]}\n'
          f'\033[0;34mPassword\033[0m:   {data[1]}\n'
          f'\033[0;34mName\033[0m:       {data[2]}\n'
          f'\033[0;34mPhone\033[0m:      {data[3]}\n'
          f'\033[0;34mGender\033[0m:     {data[4]}\n'
          f'\033[0;34mCamp\033[0m:       {data[5]}\n'
          f'\033[0;34mStatus\033[0m:     {data[6]}')


def create_Volunteer(username, password, name, phone, sex, camp, status,plan):
    path = "volunteer.json"
    volu = v.volunteer(username, password, name, phone, sex, camp, status,plan)
    data = j.read(path)["volunteer"]
    newdata = [username, password, name, phone, sex, camp, status,plan]
    data[username] = newdata
    j.write(path, {"volunteer" : data})
    path = "account.json"
    data = j.read(path)["account"]
    data[username] = password
    j.write(path, {"account" : data})
    return volu


def create_camp(name):
    data = j.read("camp.json")['camp']
    data[name] = [name,[],False]
    j.write("camp.json", {"camp":data})


def get_information_profile_camp(name):
    data = j.read('camp.json')['camp'][name]
    print(f'Camp name:    {data[0]}\n'
          f'Refugee list: {" ".join(data[1])}\n'
          f'Camp status:  {data[2]}')


def get_information_list(path):

        name = path[:-5:]
        data = j.read(path)[name]
        list = []
        for key in data:
            if data[key][2] == False:
                list.append(key)

        return list


def generate_report(e_plan):
    e_data = j.read("emergency_plan.json")["emergency_plan"]
    c_data = j.read("camp.json")["camp"]
    r_data = j.read("refugee.json")["refugee"]

    for e in e_data:
        if e == e_plan:
            cur_plan_camp = e_data[e][6]
            print('')
            print("\033[1;30;47mReport for emergency plan\033[0m " + '<' + e_data[e][0] + '>')
            print('')

            # # Table
            # b_date = e_data[e][4][0]+"-"+e_data[e][4][1]+"-"+e_data[e][4][2]
            # e_date = e_data[e][5][0]+"-"+e_data[e][5][1]+"-"+e_data[e][5][2]
            #
            # print('\033[1;34mSummary table\033[0m')
            # print('')
            #
            # # print(tabulate([[e_data[e][0], e_data[e][1], e_data[e][2], e_data[e][3], b_date, e_date]],
            # #                headers=['Name', 'Kind', 'Description', 'Region', 'Begin date', 'End date'],
            # #                tablefmt='orgtbl'))

            # Illustration
            print('')
            print('\033[1;34mName\033[0m  ' + e_data[e][0])
            print('')
            print('\033[1;34mKind\033[0m  ' + e_data[e][1])
            print('')
            print('\033[1;34mDescription\033[0m  ' + e_data[e][2])
            print('')
            print('\033[1;34mRegion\033[0m  ' + e_data[e][3])
            print('')
            print('\033[1;34mDuration\033[0m  ' + "available from "
                  + e_data[e][4][0]+"-"+e_data[e][4][1]+"-"+e_data[e][4][2] + " to "
                  + e_data[e][5][0]+"-"+e_data[e][5][1]+"-"+e_data[e][5][2])
            print('')
            print("\033[1;34mBasic information on current emergency plan camp resources\033[0m")
            print("There are " + str(len(cur_plan_camp)) + " camps in the current plan")
            print('')
            water_shortage = ""
            food_shortage = ""
            medical_shortage = ""
            water_score = []
            food_score = []
            medical_score = []
            camp_list = []
            for c in c_data:
                if c in cur_plan_camp:
                    camp1 = camp.camp(c_data[c][0], c_data[c][1], c_data[c][2])
                    water_score.append(camp1.compute_water())
                    food_score.append(camp1.compute_food())
                    camp_list.append(c)
                    medical_score.append(camp1.compute_medical())
                    if camp1.compute_medical() < 10:
                        medical_shortage += " "
                        medical_shortage += c
                    if camp1.compute_water() < 10:
                        water_shortage += " "
                        water_shortage += c
                    if camp1.compute_food() < 10:
                        food_shortage += " "
                        food_shortage += c
            mydata = [water_score, food_score, medical_score]
            # print("water", water_score)
            # print("food", food_score)
            # print("medical", medical_score)
            print(pd.DataFrame(mydata, index=['Water', 'Food', 'Medical'], columns=camp_list))
            if water_shortage != "":
                #这里是否能够用红色或者其他醒目颜色醒目一下，后面两个也是
                print("Current Water Shortage Camps: " + water_shortage)
            if food_shortage != "":
                print("Current Food Shortage Camps: " + food_shortage)
            if medical_shortage != "":
                print("Current Medical Shortage Camps: " + medical_shortage)

            total_num = 0
            refugee_data_list = []
            sex_key = [0,0]
            health_status = {"No pain": 0, "Mild pain": 0, "Moderate pain": 0, "Severe pain": 0, "Worst pain/EMERGENCY": 0}
            age_statistics = {"young": 0, "middle": 0, "old": 0}
            for r in r_data:
                if r_data[r][6] in cur_plan_camp:
                    total_num += 1
                    refugee_data_list.append([r_data[r][0], r_data[r][1], r_data[r][2], r_data[r][3], r_data[r][4], r_data[r][6]])
                    #性别数量
                    if r_data[r][2] == True:
                        sex_key[0] = sex_key[0] + 1
                    else:
                        sex_key[1] = sex_key[1] + 1

                    #健康状态统计
                    health_status[r_data[r][4]] += 1

                    #年龄统计
                    if r_data[r][3] <= 20:
                        age_statistics["young"] += 1
                    elif r_data[r][3] > 20 and r_data[r][3] <= 60:
                        age_statistics["middle"] += 1
                    else:
                        age_statistics["old"] += 1

            print('')
            print("\033[1;34mThe Current Basic Information of Refugee Statistic\033[0m")
            if total_num != 0:
                print("Gender composition: ", end="")
                print("\033[0;34mMale\033[0m ", "%.2f"%((sex_key[0]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;31m  Female\033[0m ", "%.2f"%((sex_key[1]/total_num)*100), end="")
                print("%", end="")
                print("")

                print("Health Status composition: ", end="")
                print("\033[0;37mNo pain\033[0m ", "%.2f"%((health_status["No pain"]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;32m  Mild pain\033[0m ", "%.2f"%((health_status["Mild pain"]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;34m  Moderate pain\033[0m ", "%.2f"%((health_status["Moderate pain"]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;33m  Severe pain\033[0m ", "%.2f"%((health_status["Severe pain"]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;31m  Worst pain/EMERGENCY\033[0m ", "%.2f"%((health_status["Worst pain/EMERGENCY"]/total_num)*100), end="")
                print("%", end="")
                print("")

                print("Age composition: ", end="")
                print("\033[0;32mYoung group [<20]\033[0m ", "%.2f"%((age_statistics["young"]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;34m  Middle-aged group [20-60]\033[0m ", "%.2f"%((age_statistics["middle"]/total_num)*100), end="")
                print("%", end="")
                print("\033[0;37m  Elder group [>60]\033[0m ", "%.2f"%((age_statistics["old"]/total_num)*100), end="")
                print("%", end="")
                print("")
            print('')
            print(pd.DataFrame(refugee_data_list, columns=['Name', 'Phone', 'Gender', 'Age', 'Health Status', 'Camp']))
            print('')
            print('')


