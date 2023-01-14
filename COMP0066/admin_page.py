import utilities
import js as j
import volunteer as v
from admin import admin
import datetime
import login
import numpy as np


def page_admin():
    all_plans = []
    for i in utilities.get_information("emergency_plan.json"):
        all_plans.append(i)

    for i in all_plans:
        data = j.read('emergency_plan.json')['emergency_plan'][i]
        data_camp = []  # refugee数量
        data_vltr = []
        v_data = j.read('volunteer.json')['volunteer']

        for camp in data[6]:  # camp数量
            data_camp.append(j.read('camp.json')['camp'][camp][1])

        if len(data[6]) == 0:
            print(f'\033[1mPlan "{i}" may need more camps for refugees.\033[0m')

        elif len(data_camp) / len(data[6]) > 10:
            print(f'\033[1mPlan "{i}" may need more camps for refugees.\033[0m')

        for vltr in v_data:
            if v_data[vltr][5] == i:
                data_vltr.append(v_data[vltr][5])

        if len(data_vltr) == 0:
            print(f'\033[1mPlan "{i}" may need more volunteer to manage.\033[0m')

        elif len(data[6]) / len(data_vltr) > 5:
            print(f'\033[1mPlan "{i}" may need more volunteer to manage.\033[0m')

    print('')
    print("\033[1;30;47mHi, administer. Welcome to the humanitarian emergency management system.\033[0m")
    print('\033[0;35m[ 1 ]\033[0m' + ' Act on emergency plans')
    print('\033[0;35m[ 2 ]\033[0m' + ' Act on volunteer account information')
    print('\033[0;35m[ 3 ]\033[0m' + ' Act on camps setting')
    print('\033[0;35m[ 4 ]\033[0m' + ' Log out')
    print('')

    decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')
    if decision.isdigit():
        if int(decision) == 1:
            edit_emergency_plan()
            print('')

        if int(decision) == 2:
            volunteer_change()
            print('')

        if int(decision) == 3:
            change_camp()
            print('')

        if int(decision) == 4:
            while True:
                # try:
                print('')
                print("\033[1;30;47mRole Selection\033[0m")
                print("Log in as " + "\033[4;34mAdmin (A/a)\033[0m" + " or " + "\033[4;34mVolunteer (V/v)\033[0m" + ' ?')
                role = input("Your " + "\033[4;34mrole\033[0m" + " is: ")
                # print("Welcome to the humanitarian emergency management system.")
                if role == "A" or role == "a" or role == "admin" or role == "Admin":
                    print('')
                    login.admin_login()
                    break
                elif role == "V" or role == "v" or role == "volunteer" or role == "Volunteer":
                    print('')
                    login.vol_login()
                    break
                else:
                    print("\033[1;31mPlease enter a valid word.\033[0m")

        else:
            print('')
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please enter a valid word.")
            page_admin()

    else:
        print('')
        print("\033[1;31mInvalid action\033[0m\n"
              "Please enter a valid word.")
        page_admin()


def edit_emergency_plan(admin=admin('zhangsan', 111, True, 20, 'admin', 111)):
    print('')
    print(f'\033[1;36mCurrent emergency plans:\033[0m')

    # show the current emergency plan
    a = 1
    for i in utilities.get_information("emergency_plan.json"):
        print(f'[ {a} ] {i}')
        a += 1

    print('')
    print('\033[1;30;47mAction available:\033[0m')
    print('\033[0;35m[ 1 ]\033[0m Create a new emergency plan\n'
          '\033[0;35m[ 2 ]\033[0m Edit the emergency plan\n'
          '\033[0;35m[ 3 ]\033[0m View the emergency plan profile\n'
          '\033[0;35m[ 4 ]\033[0m Back to the welcome page.')
    print('')
    while True:
        decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')
        print('')

        if decision.isdigit():

            if int(decision) == 1:
                print('\033[1;30;47mPlan creating:\033[0m')
                while True:
                    e_name = input('\033[0;34mName\033[0m: ')
                    if e_name not in utilities.get_information("emergency_plan.json"):
                        break
                    else:
                        print("\033[1;31mDuplicate plan name, try another name\033[0m\n")
                e_kind = input('\033[0;34mKind\033[0m: ')
                e_des = input('\033[0;34mDescription\033[0m: ')
                e_region = input('\033[0;34mRegion\033[0m: ')
                print('')

                camp = j.read("camp.json")["camp"]
                e_camps = []

                condition = True
                while condition:
                    print(f'\033[1;36mCurrent camps\033[0m: ')

                    a = 1
                    for i in utilities.get_information_list("camp.json"):
                        print(f'[ {a} ] {i}')
                        a += 1

                    print('Please input camp name to add or input[x]to not add camp.')
                    e_camp = input('\033[0;34mCamp\033[0m: ')
                    if e_camp=='x':
                        e_camps= []
                        break
                    else:

                        if e_camp not in utilities.get_information_list("camp.json"):
                            print("\033[1;31mInvalid action\033[0m\n"
                                  "Please enter a valid word.")
                            print('')

                        elif e_camp in utilities.get_information("camp.json") and e_camp not in e_camps:
                            e_camps.append(e_camp)
                            add_more = input('\033[0;34mWould you like to add another camp? (y/n)\033[0m: ')
                            print('')

                            if add_more == 'n' or add_more == 'no' or add_more == 'No':
                                condition = False

                        elif e_camp in utilities.get_information("camp.json") and e_camp in e_camps:
                            print("\033[0;31mThis camp already in the emergency plan!\033[0m\n")
                            print('')

                # 初始时间
                while True:
                    print('')
                    print('\033[0;34mBegin date\033[0m')
                    year = input('\033[0;34mYear\033[0m: ')
                    month = input('\033[0;34mMonth\033[0m: ')
                    day = input('\033[0;34mDay\033[0m: ')
                    if year.isdigit() and month.isdigit() and day.isdigit():
                        if len(year) == 4 and 1<=int(month)<=12 and int(day)<=31:
                           break
                        else:
                            print("\033[1;31mInvalid action\033[0m\n"
                                  "Please enter a legal date.")
                    else:
                        print("Please enter a legal date.")
                e_b_date = datetime.date(int(year), int(month), int(day))

                # print('')
                # print('\033[0;34mEnd date\033[0m')
                # year = int(input('\033[0;34mYear\033[0m: '))
                # month = int(input('\033[0;34mMonth\033[0m: '))
                # day = int(input('\033[0;34mDay\033[0m: '))
                # e_e_date = datetime.date(year, month, day)

                admin.create_emergency_plan(e_name, e_kind, e_des, e_region,
                                            e_b_date, camps=e_camps)

                data = j.read('camp.json')["camp"]

                for i in e_camps:
                    data[i][2] = True

                j.write('camp.json', {"camp": data})

                print('')
                page_admin()  # 返回主菜单

            if int(decision) == 2:
                write_emergency_data()

            if int(decision) == 3:
                a = 1
                campsnow = []

                print(f'\033[1;36mCurrent emergency plans:\033[0m')
                for i in utilities.get_information("emergency_plan.json"):
                    print(f'[ {a} ] {i}')
                    campsnow.append(i)
                    a += 1

                while True:
                    print('')
                    number = input('\033[0;34mName\033[0m of the plan viewed: ')
                    if number in campsnow:
                        print('')
                        utilities.get_information_profile(number)
                        con = False
                        print('')

                        checked = input('Press any button to continue (back to the welcome page) => ')
                        if checked == '1':
                            print('')
                            print('Back to the welcome page...')
                            print('')
                            page_admin()
                        else:
                            print('')
                            print('Back to the welcome page...')
                            print('')
                            page_admin()

                        break

                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please enter a valid word.\n\n")

            if int(decision) == 4:
                page_admin()

            else:
                print('')
                print("\033[1;31mInvalid action\033[0m\n"
                      "Please enter a valid word.")
                print('')
                edit_emergency_plan()

        else:
            print('')
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please enter a valid word.")
            print('')
            page_admin()


def write_emergency_data(admin=admin('zhangsan', 111, True, 20, 'admin', 111)):
    a = 1
    print(f'\033[1;36mCurrent emergency plans:\033[0m')
    for i in utilities.get_information("emergency_plan.json"):
        print(f'[ {a} ] {i}')
        a += 1

    data = j.read('emergency_plan.json')["emergency_plan"]
    key_list = [*data]
    print('')

    while True:
        name = input('\033[0;34mName\033[0m of the plan need to edit.\n'
                     'The emergency plan is: ')

        print('')
        if name in key_list:
            break
        else:
            print("\033[1;31mInvalid name\033[0m\n"
                  "Please enter a valid name.")
            print('')
            write_emergency_data()

    decision = input("\033[1;30;47mInformation available to edit\033[0m\n"
                     "\033[0;35m[ 1 ]\033[0m Name\n"
                     "\033[0;35m[ 2 ]\033[0m Kind\n"
                     "\033[0;35m[ 3 ]\033[0m Description\n"
                     "\033[0;35m[ 4 ]\033[0m Region\n"
                     "\033[0;35m[ 5 ]\033[0m Begin date\n"
                     "\033[0;35m[ 6 ]\033[0m End date\n"
                     "\033[0;35m[ 7 ]\033[0m Camp\n"
                     "\033[0;35m[ 8 ]\033[0m Delete the plan\n"
                     "\033[0;35m[ 9 ]\033[0m Back to home\n"
                     "\n"
                     'Select an ' + '\033[0;34maction\033[0m' ': ')

    print('')

    if decision == '1':
        new_info = input('The \033[0;34mnew name\033[0m is: ')
        data[name][0] = new_info  # imp字段对应的deeplink的值修改为end
        j.write('emergency_plan.json', {"emergency_plan": data})
        # back to welcome page
        print('')
        print('\033[1;32mEdit successfully.\033[0m')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return

    if decision == '2':
        new_info = input('The \033[0;34mnew kind\033[0m is: ')
        data[name][1] = new_info  # imp字段对应的deeplink的值修改为end
        j.write('emergency_plan.json', {"emergency_plan": data})
        # back to welcome page
        print('')
        print('\033[1;32mEdit successfully.\033[0m')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return

    if decision == '3':
        new_info = input('The \033[0;34mnew description\033[0m is: ')
        data[name][2] = new_info  # imp字段对应的deeplink的值修改为end
        j.write('emergency_plan.json', {"emergency_plan": data})
        # back to welcome page
        print('')
        print('\033[1;32mEdit successfully.\033[0m')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return

    if decision == '4':
        new_info = input('The \033[0;34mnew region\033[0m is: ')
        data[name][3] = new_info  # imp字段对应的deeplink的值修改为end
        j.write('emergency_plan.json', {"emergency_plan": data})
        # back to welcome page
        print('')
        print('\033[1;32mEdit successfully.\033[0m')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return

    if decision == '5':
        while True:
            print('')
            print('\033[0;34mBegin date\033[0m')
            year = input('\033[0;34mYear\033[0m: ')
            month = input('\033[0;34mMonth\033[0m: ')
            day = input('\033[0;34mDay\033[0m: ')
            if year.isdigit() and month.isdigit() and day.isdigit():
                break
            else:
                print("Please input a Legal time")
        new_date = [year, month, day]
        data[name][4] = new_date  # imp字段对应的deeplink的值修改为end
        j.write('emergency_plan.json', {"emergency_plan": data})
        # back to welcome page
        print('')
        print('\033[1;32mEdit successfully.\033[0m')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return

    if decision == '6':

            while True:
                while True:
                    begin_date = data[name][4]
                    begin_date_string = begin_date[0]+begin_date[1]+begin_date[2]
                    print('\033[0;34mEnd date\033[0m')
                    year = input('\033[0;34mYear\033[0m: ')
                    month = input('\033[0;34mMonth\033[0m: ')
                    day = input('\033[0;34mDay\033[0m: ')
                    if year.isdigit() and month.isdigit() and day.isdigit():
                        break
                    else:
                        print("\033[1;31mInput pure int number\033[0m\n")

                if len(month) == 1:
                    month = '0' + month
                if len(day) == 1:
                    day = '0' + day
                end_date_string = year+month+day

                if len(year) != 4:
                    print("\033[1;31mInput a valid year date\033[0m\n")

                elif int(month) > 12 or int(month) < 1:
                    print("\033[1;31mInput a valid month date\033[0m\n")

                elif int(day) > 31:
                    print("\033[1;31mInput a valid day date\033[0m\n")

                elif int(end_date_string) <= int(begin_date_string):
                    print("\033[1;31mEnd date cannot earlier than start date\033[0m\n")
                else:
                    break

            new_date = [year, month, day]
            data[name][5] = new_date  # imp字段对应的deeplink的值修改为end
            j.write('emergency_plan.json', {"emergency_plan": data})
            # back to welcome page
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_admin()
            return

    if decision == '7':
        campnow = j.read('emergency_plan.json')["emergency_plan"][name][6]
        print(f'\033[1;36mCurrent camps in this plan\033[0m: ')

        a = 1
        for i in campnow:
            print(f'[ {a} ] {i}')
            a += 1

        while True:
            choice = input('\033[1;30;47mAction available\033[0m\n'
                           '\033[0;34m[ 1 ]\033[0m Add camps\n'
                           '\033[0;34m[ 2 ]\033[0m Delete camps\n'
                           '\033[0;34m[ 3 ]\033[0m Back to welcome page\n'
                           'Select an ' + '\033[0;34maction\033[0m' ': ')

            if choice == '1':

                campnow = j.read('emergency_plan.json')["emergency_plan"][name][6]
                campadd = []
                condition = True

                while condition:
                    print(f'\033[1;36mCurrent empty camp\033[0m: ')

                    a = 1
                    for i in utilities.get_information_list("camp.json"):
                        print(f'[ {a} ] {i}')
                        a += 1

                    new_info = input('\033[0;34mName\033[0m of the camp add or print[x] to back to home page: ')

                    if new_info == 'x':
                        page_admin()
                        break
                    else:
                        if new_info in utilities.get_information_list("camp.json"):
                            campadd.append(new_info)

                        if new_info not in utilities.get_information_list("camp.json"):
                            print("\033[1;31mInvalid name\033[0m\n"
                                  "Please enter a valid name.")
                            print('')

                        condition = True
                        print('')
                        print('\033[0;34mWould you like to add another camp? (y/n)\033[0m: ')
                        print('')

                        add_more = input('Select an ' + '\033[0;34maction\033[0m' ': ')
                        if add_more == 'n' or add_more == 'no' or add_more == 'No':
                            condition = False

                    campall = campadd + campnow  # imp字段对应的deeplink的值修改为end
                    data[name][6] = campall
                    j.write('emergency_plan.json', {"emergency_plan": data})
                    datacamp = j.read('camp.json')["camp"]

                    for i in campall:
                        datacamp[i][2] = True
                        j.write('camp.json', {"camp": datacamp})

                    print('')
                    print('\033[1;32mEdit successfully.\033[0m')
                    print('Back to the welcome page...')
                    print('')
                    page_admin()  # 返回主菜单
                    break
            if choice == '2':
                datacamp = j.read('camp.json')["camp"]
                campnow = j.read('emergency_plan.json')["emergency_plan"][name][6]

                while True:
                    deletecamp = input('\033[0;34mName\033[0m of the camp delete or input[x] to back to home page: ')
                    if deletecamp== 'x':
                        page_admin()
                        break
                    else:

                        if deletecamp not in campnow:
                            print("\033[1;31mNot exist in the plan\033[0m\n"
                                  "Please enter a valid name.")

                        else:
                            for i in campnow:
                                if i == deletecamp:
                                    campnow.remove(deletecamp)

                            data[name][6] =campnow
                            j.write('emergency_plan.json', {"emergency_plan": data})
                            datacamp[deletecamp][2] = False
                            j.write('camp.json', {"camp": datacamp})

                            print('')
                            print('\033[1;32mEdit successfully.\033[0m')
                            print('Back to the welcome page...')
                            print('')
                            page_admin()
                            break
            if choice == '3':
                print('Back to the welcome page...')
                page_admin()
                break
            else:
                print("\033[1;31mNot legal choice\033[0m\n")


    if decision == '8':
        admin.del_plan(name)
        print('')
        print('\033[1;32mEdit successfully.\033[0m')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return

    if decision == '9':
        print('')
        print('Back to the welcome page...')
        print('')
        page_admin()
        return
    else:
        print("\033[1;31mInvalid name\033[0m\n"
              "Please enter a valid name.")
        print('')
        page_admin()


def volunteer_change(admin = admin('zhangsan',111, True, 20, 'admin', 111)):

    condition = True

    print('')
    while (condition):
        a = 1
        print(f'\033[1;36mCurrent volunteer profiles\033[0m: ')
        for i in utilities.get_information("volunteer.json"):
            print(f'[ {a} ] {i}')
            a += 1

        print('')

        print('\033[1;30;47mAction available:\033[0m\n'
              '\033[0;35m[ 1 ]\033[0m Create a new volunteer account\n'
              '\033[0;35m[ 2 ]\033[0m Deactivate/Delete a volunteer account\n'
              '\033[0;35m[ 3 ]\033[0m Reactivate a volunteer account\n'
              '\033[0;35m[ 4 ]\033[0m View volunteer profiles\n'
              '\033[0;35m[ 5 ]\033[0m Arrange plan for no-work volunteer\n'
              '\033[0;35m[ 6 ]\033[0m Back to the welcome page')
        print('')

        decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')  # c
        print('')

        if decision.isdigit():

            if int(decision) == 1:
                while True:
                    v_username = input('\033[0;34mUsername\033[0m: ')  # a
                    if v_username not in utilities.get_information("volunteer.json"):
                        break
                    else:
                        print("\033[1;31mDuplicate volunteer name, try another name\033[0m\n")
                v_password = input('\033[0;34mPassword\033[0m: ')  # b
                v_name = input('\033[0;34mName\033[0m: ')  # c
                v_contact = input('\033[0;34mContact number\033[0m: ')  # d

                while True:
                    gender = input('\033[0;34mGender (m/f)\033[0m: ')  # sex
                    if gender == 'm' or gender == 'M' or gender == 'male':
                        v_gender = True  # e
                        break
                    elif gender == 'f' or gender == 'F' or gender == 'female':
                        v_gender = False
                        break
                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please enter a valid word.")
                        print('')

                list = utilities.get_information("camp.json")
                print('')

                a = 1
                print(f'\033[1;36mCurrent emergency plans\033[0m: ')
                for i in utilities.get_information("emergency_plan.json"):
                    print(f'[ {a} ] {i}')
                    a += 1

                print('')
                while True:
                    v_plan = input('\033[0;34mEmergency plan\033[0m: ')  # f

                    if v_plan in utilities.get_information("emergency_plan.json"):
                        break
                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please enter a valid word.")
                        print('')

                while True:
                    status = input('\033[0;34mStatus of the volunteer (t/f)\033[0m: ')

                    if status == 't' or status == 'T':
                        v_status = True  # g
                        break
                    elif status == 'f' or status == 'F':
                        v_status = False
                        break
                    else:
                        print('')
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please enter a valid word.")
                        print('')

                admin.create_Volunteer(v_username, v_password, v_name,
                                       v_contact, v_gender, v_plan, v_status)

                print('')
                print('\033[1;32mCreate successfully.\033[0m')
                print('')
                condition = False
                page_admin()

            elif int(decision) == 2:

                print('')

                a = 1
                print(f'\033[1;36mCurrent volunteer profiles\033[0m: ')
                for i in utilities.get_information("volunteer.json"):
                    print(f'[ {a} ] {i}')
                    a += 1

                print('')
                con = True
                while(con):

                    print('\033[1;30;47mAction available:\033[0m\n'
                          '\033[0;34m[ 1 ]\033[0m Deactivate an account\n'
                          '\033[0;34m[ 2 ]\033[0m Delete an account')
                    print('')

                    # Input 1 to deactivate, Input 2 to delete

                    decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')  # a

                    if decision == '1':
                        while True:
                            de_name = input('\033[0;34mDeactivate username\033[0m: ')  # b
                            data = j.read("volunteer.json")["volunteer"]
                            keyl = [*data]

                            if de_name in keyl:
                                for key in data:
                                    if key == de_name:
                                        volu = v.volunteer(data[key][0], data[key][1], data[key][2],
                                                           data[key][3], data[key][4],
                                                           data[key][5], data[key][6])

                                        admin.stop_Volunteer(volu)
                                        print('')
                                        print('\033[1;32mDeactivate successfully.\033[0m')
                                        print('')
                                        # con = False
                                        break
                                volunteer_change(admin)
                                break

                            else:
                                print('')
                                print('\033[1;31mDeactivate unsuccessfully.\033[0m')
                                print('')

                    elif decision == '2':
                        print('')
                        del_name = input('\033[0;34mDeleted username\033[0m: ')  # b

                        if del_name != "admin":
                            data = j.read("volunteer.json")["volunteer"]
                            keyl = [*data]
                            if del_name in keyl:
                                for key in data:
                                    if key == del_name:
                                        volu = v.volunteer(data[key][0], data[key][1], data[key][2],
                                                           data[key][3], data[key][4],
                                                           data[key][5], data[key][6])
                                        admin.delete_Volunteer(volu)
                                        print('')
                                        print('\033[1;32mDelete successfully.\033[0m')
                                        print('')
                            else:
                                print('')
                                print('\033[1;31mDelete unsuccessfully.\033[0m')
                                print('')

                        else:
                            print('')
                            print('\033[1;31mDelete unsuccessfully.\033[0m')
                            print('')
                        con = False

                    else:
                        print('')
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please enter a valid word.")
                        print('')

            elif int(decision) == 3:
                dead_vltr = []
                print('')
                a = 1
                print(f'\033[1;36mCurrent deactive volunteer profiles\033[0m: ')

                for i in utilities.get_information("volunteer.json"):
                    if j.read("volunteer.json")["volunteer"][i][6] == False:
                        print(f'[ {a} ] {i}')
                        a += 1
                        dead_vltr.append(i)

                print('')
                while True:
                    rea_name = input('\033[0;34mName reactivate\033[0m: ')  # a
                    data = j.read("volunteer.json")["volunteer"]
                    keyl = [*data]
                    if rea_name == 'x':
                        con = False
                        break

                    if rea_name in dead_vltr:
                        for key in data:
                            if key == rea_name:
                                volu = v.volunteer(data[key][0], data[key][1],
                                                   data[key][2], data[key][3],
                                                   data[key][4], data[key][5], data[key][6])
                                admin.reactive_Volunteer(volu)
                                print('')
                                print('\033[1;32mReactive successfully.\033[0m')
                                print('')
                        con = False
                        break
                    else:
                        print('')
                        print('\033[1;31mPlease input correct name\033[0m')
                        print('')

                volunteer_change()

            elif int(decision) == 4:
                print('')
                a = 1
                print(f'\033[1;36mCurrent volunteer profiles\033[0m: ')
                for i in utilities.get_information("volunteer.json"):
                    print(f'[ {a} ] {i}')
                    a += 1
                print('')
                while True:
                    name = input('The \033[0;34mvolunteer username\033[0m viewed: ')
                    if name not in utilities.get_information("volunteer.json"):
                        print('')
                        print("\033[1;31mInvalid action\033[0m\n"
                        "Please enter a valid word.")
                    else:
                        break

                utilities.get_information_profile_volunteer(name)
                condition = False
                print('')

                checked = input('Press any button to continue (back to the welcome page) => ')
                if checked == '1':
                    print('')
                    print('Back to the welcome page...')
                    print('')
                    page_admin()
                else:
                    print('')
                    print('Back to the welcome page...')
                    print('')
                    page_admin()

            elif int(decision) == 5:
                print('')
                condition = False
                re_work()
            elif int(decision) == 6:
                print('')
                condition = False
                page_admin()
            else:
                print("\033[1;31mInvalid action\033[0m\n"
                      "Please enter a valid word.")
                print('')
                page_admin()

        else:
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please enter a valid word.")
            print('')
            page_admin()

    return


def change_camp():
    print('')
    print('\033[1;30;47mAction available:\033[0m\n'
          '\033[0;34m[ 1 ]\033[0m Create a new camp\n'
          '\033[0;34m[ 2 ]\033[0m View the camp\n'
          '\033[0;34m[ 3 ]\033[0m Back to the welcome page')
    print('')

    while True:
        decision = input('Select an ' + '\033[0;34maction\033[0m: ')  # a
        print('')
        if decision.isdigit():

            if int(decision) == 1:
                while True:
                    name = input('\033[0;34mCamp name\033[0m: ')

                    if name not in utilities.get_information("camp.json"):
                        utilities.create_camp(name)
                        print('')
                        print('\033[1;32mCreate successfully.\033[0m')
                        print('')
                        change_camp()
                        break

                    if name in utilities.get_information("camp.json"):
                        print('')
                        print('\033[1;31mUnsuccessfully, the name has been used.\033[0m')
                        print('')


            if int(decision) == 2:
                print('')
                while True:

                    a = 1
                    print(f'\033[1;36mCurrent camps ID:\033[0m')
                    for i in utilities.get_information("camp.json"):
                        print(f'[ {a} ] {i}')
                        a += 1

                    print('')
                    name = input('\033[0;34mInput camp ID to viewed\033[0m: ')

                    if name in utilities.get_information("camp.json"):
                        utilities.get_information_profile_camp(name)
                        print('')

                        checked = input('Press any button to continue (back to the welcome page) => ')

                        if checked == '1':
                            print('')
                            print('Back to the welcome page...')
                            print('')
                            page_admin()
                            break
                        else:
                            print('')
                            print('Back to the welcome page...')
                            print('')

                        page_admin()
                        break

                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please enter a valid word.")
                        print('')
                break
            if int(decision) == 3:
                print('')
                page_admin()
                break

            else:
                print("\033[1;31mInvalid action\033[0m\n"
                      "Please enter a valid number.")
                print('')

        else:
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please enter a valid number.")
            print('')

def re_work():
    data = j.read('volunteer.json')['volunteer']
    nowork_list=[]
    for i in data:
        if data[i][5]=='No Work':
            nowork_list.append(i)

    print('')
    a = 1
    print(f'\033[1;36mCurrent  no work volunteer list\033[0m: ')
    for i in nowork_list:
        print(f'[ {a} ] {i}')
        a += 1
    print('')
    while True:
        name = input('Input the \033[0;34mvolunteer username\033[0m to arrange work or input [x] to back: ')
        if name == 'x':
            page_admin()
            break
        elif name not in nowork_list:
            print("\033[1;31mInvalid action\033[0m\n"
                  "Username not in the list.")
            print('')
        else:
            plan_list=[]
            print('')
            print(f'\033[1;36mCurrent emergency plans:\033[0m')

            # show the current emergency plan
            a = 1
            for i in utilities.get_information("emergency_plan.json"):
                print(f'[ {a} ] {i}')
                plan_list.append(i)
                a += 1
            while True:
                plan_name=input('The \033[0;34mplan name\033[0m to arrange work: ')
                if plan_name not in plan_list:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please enter a valid plan name.")
                    print('')
                else:
                    data[name][5]=plan_name
                    j.write('volunteer.json', {"volunteer": data})
                    print('')
                    print('Back to welcome page...')
                    print('')
                    page_admin()
                    break



