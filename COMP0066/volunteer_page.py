import utilities
import js as j
from refugee import refugee
import login

# Health status choice
health_status = {1: "No pain",
                 2: "Mild pain",
                 3: "Moderate pain",
                 4: "Severe pain",
                 5: "Worst pain/EMERGENCY"}


def page_volunteer(volunteer):
    print("\033[1;30;47mHi, volunteer. Welcome to the humanitarian emergency management system.\033[0m")
    print('\033[0;35m[ 1 ]\033[0m' + ' Act on the volunteer profile')
    print('\033[0;35m[ 2 ]\033[0m' + ' Act on the refugee emergency profile')
    # print('\033[0;35m[ 3 ]\033[0m' + ' Edit the refugee emergency profile directly')
    print('\033[0;35m[ 3 ]\033[0m' + ' Generate the emergency plan report')
    print('\033[0;35m[ 4 ]\033[0m' + ' Edit the camp identification of current emergency plan')
    print('\033[0;35m[ 5 ]\033[0m' + ' Log out')
    print('')
    while True:
        decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')
        if decision.isdigit():
            print('')
            if int(decision) == 1:
                volunteer_profile(volunteer)
                print('')

            elif int(decision) == 2:
                create_refugee_profile(volunteer)
                print('')

            # elif int(decision) == 3:
            #     print(f'\033[1;36mCurrent refugee profiles:\033[0m')
            #
            #     a = 1
            #     for i in utilities.get_information("refugee.json"):
            #         print(f'{a} - {i}')
            #         a += 1
            #
            #     print('')
            #     # read file refugee.json
            #     data = j.read("refugee.json")["refugee"]
            #     # select data as key list
            #     key_list = [*data]
            #
            #     # detect the name exist or not
            #     while True:
            #         name = input('Enter the \033[0;34mrefugee name\033[0m you want to edit.\n'
            #                      'The \033[0;34mrefugee name\033[0m is: ')
            #         if name in key_list:
            #             break
            #         else:
            #             create_refugee_profile(volunteer)  # jump to create refugee
            #
            #     detail = data[name]
            #
            #     # 0 - refugee name
            #     # 1 - refugee mobile phone number
            #     # 2 - refugee gender (True -> male, False -> female)
            #     # 3 - refugee age
            #     # 4 - refugee status
            #     # 5 - refugee camp
            #
            #     r = refugee(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5])
            #     print('')
            #     edit_refugee_details(r, volunteer)

            elif int(decision) == 3:
                v_data = j.read("volunteer.json")["volunteer"]
                plan_name = v_data[volunteer.getUserName()][5]
                if plan_name != "No Work":
                    utilities.generate_report(plan_name)
                else:
                    print("You do not have seperated the camp")

                page_volunteer(volunteer)

            elif int(decision) == 4:
                e_data = j.read("emergency_plan.json")["emergency_plan"]
                v_data = j.read("volunteer.json")["volunteer"]
                c_data = j.read("camp.json")["camp"]
                r_data = j.read("refugee.json")["refugee"]

                plan_name = v_data[volunteer.getUserName()][5]
                camp_list = e_data[plan_name][6]
                print('\033[1;36mCurrent existing camp in the current emergency plan\033[0m: \n'
                      '', end="")

                for c in camp_list:
                    print(c+" ", end="")

                print("")

                while True:
                    edit_camp = input("The \033[0;34mcamp\033[0m which you want to edit: ")
                    if edit_camp in camp_list:
                        break
                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please select a valid action.")
                while True:
                    new_name = input("Please input the new name: ")
                    if new_name not in [*c_data]:
                        break
                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please select a valid name.")
                camp_list.remove(edit_camp)
                camp_list.append(new_name)
                e_data[plan_name][6] = camp_list
                j.write("emergency_plan.json", {"emergency_plan": e_data})
                for r in r_data:
                    if r_data[r][6] == edit_camp:
                        r_data[r][6] = new_name
                j.write("refugee.json", {"refugee": r_data})

                for c in c_data:
                    if c == edit_camp:
                        camp_info = c_data[c]
                del c_data[edit_camp]

                camp_info[0] = new_name
                c_data[new_name] = camp_info
                j.write("camp.json", {"camp": c_data})

                print('')
                print('\033[1;32mEdit successfully.\033[0m')
                print('')
                page_volunteer(volunteer)

            elif int(decision) == 5:
                while True:
                    # try:
                    print('')
                    print("\033[1;30;47mRole Selection\033[0m")
                    print(
                        "Log in as " + "\033[4;34mAdmin (A/a)\033[0m" + " or " + "\033[4;34mVolunteer (V/v)\033[0m" + ' ?')
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

                # login.vol_login()  # Log out !!!!!!

            else:
                print("\033[1;31mInvalid action\033[0m\n"
                      "Please select a valid action.")

        else:
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please select a valid action.")


def volunteer_profile(volunteer):
    # print('')
    # print(f'\033[1;36mVolunteer list:\033[0m\n' f''f'{utilities.get_information("volunteer.json")}')
    print('\033[1;30;47mAction available:\033[0m')
    print('\033[0;35m[ 1 ]\033[0m' + ' Edit your volunteer profile')
    print('\033[0;35m[ 2 ]\033[0m' + ' Check your information')
    print('\033[0;35m[ 3 ]\033[0m' + ' Back to the welcome page')

    while True:
        decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')
        if decision.isdigit():
            if int(decision) == 1:
                edit_volunteer_profile(volunteer)
                break
            elif int(decision) == 2:
                print('')
                check_volunteer_profile(volunteer)
                break
            elif int(decision) == 3:
                print('')
                page_volunteer(volunteer)
            else:
                print("\033[1;31mInvalid action\033[0m\n"
                      "Please select a valid action: ")
        else:
            page_volunteer(volunteer)


def check_volunteer_profile(volunteer):
    print('\033[1;30;47mYour personal profile is shown below.\033[0m')
    # read volunteer info => get volunteer info
    data = j.read("volunteer.json")["volunteer"]
    # read emergency plan info => show the camps under this emergency plan
    e_data = j.read('emergency_plan.json')

    if data[volunteer.getUserName()][4] is True:
        v_gender = 'male ♂'
    else:
        v_gender = 'female ♀'

    # 展示volunteer信息
    print("\033[0;34mName\033[0m: " + data[volunteer.getUserName()][2] + "\n"
          "\033[0;34mContact number\033[0m: " + data[volunteer.getUserName()][3] + "\n"
          "\033[0;34mGender\033[0m: " + v_gender + "\n"
          "\033[0;34mEmergency plan\033[0m: " + str(data[volunteer.getUserName()][5]))
    # 存在的volunteer emergency plan
    v_plan = data[volunteer.getUserName()][5]

    if v_plan in e_data['emergency_plan']:
        print('\033[0;34mThe camps in this emergency plan\033[0m:')
        print(e_data['emergency_plan'][v_plan][6])

    while True:
        print('')
        checked = input('Press any button to continue (back to the welcome page) => ')
        if checked.isdigit():
            if checked == '1':
                print('')
                print('Back to the welcome page...')
                print('')
                volunteer_profile(volunteer)
                break
            else:
                print('')
                print('Back to the welcome page...')
                print('')
                volunteer_profile(volunteer)
                break
        else:
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please select a valid action.")
            page_volunteer(volunteer)


def edit_volunteer_profile(volunteer):
    print('')
    print('\033[1;30;47mYou can edit your personal profile here.\033[0m')
    data = j.read("volunteer.json")["volunteer"]
    # read emergency plan info => show the camps under this emergency plan
    e_data = j.read('emergency_plan.json')

    if data[volunteer.getUserName()][4] is True:
        v_gender = 'male ♂'
    else:
        v_gender = 'female ♀'

    # 展示volunteer信息
    print("\033[0;34mName\033[0m: " + data[volunteer.getUserName()][2] + "\n"
          "\033[0;34mContact number\033[0m: " + data[volunteer.getUserName()][3] + "\n"
          "\033[0;34mGender\033[0m: " + v_gender + "\n"
          "\033[0;34mEmergency plan\033[0m: " + str(data[volunteer.getUserName()][5]))
    # 存在的volunteer emergency plan
    v_plan = data[volunteer.getUserName()][5]

    if v_plan in e_data['emergency_plan']:
        print('\033[0;34mThe camps in this emergency plan\033[0m:')
        print(e_data['emergency_plan'][v_plan][6])

    print('')
    decision = input('\033[1;30;47mSelect the number of information you want to change:\033[0m\n'
                     '\033[0;35m[ 1 ]\033[0m' + ' Name\n'
                     '\033[0;35m[ 2 ]\033[0m' + ' Contact number\n'
                     '\033[0;35m[ 3 ]\033[0m' + ' Gender\n'
                     '\033[0;35m[ 4 ]\033[0m' + ' Back to the welcome page\n'
                     ''
                     'Select an ' + '\033[0;34maction\033[0m' ': ')

    while True:
        if decision == "1":
            c_data = j.read("camp.json")["camp"]
            print('')
            print('\033[1;30;47mEditing\033[0m')

            while True:
                new_edition = input('The ' + '\033[0;34mnew name\033[0m is: ')
                if new_edition not in [*c_data]:
                    break
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please select a valid Name.")

            volunteer.setName(new_edition)
            data[volunteer.getUserName()][2] = new_edition
            j.write("volunteer.json", {"volunteer": data})
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == "2":
            print('')
            print('\033[1;30;47mEditing\033[0m')
            new_edition = input('The ' + '\033[0;34mnew contact number\033[0m is: ')
            data[volunteer.getUserName()][3] = new_edition
            j.write("volunteer.json", {"volunteer": data})
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == "3":
            while True:
                print('')
                print('\033[1;30;47mEditing\033[0m')
                gender = input('The ' + '\033[0;34mnew gender\033[0m is (male/female): ')
                if gender == "male" or gender == 'm' or gender == 'M' or gender == 'Male':
                    new_edition = True
                    break
                elif gender == "female" or gender == 'f' or gender == 'F' or gender == 'Female':
                    new_edition = False
                    break
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please enter a valid word.")

            volunteer.setSex(new_edition)
            data[volunteer.getUserName()][4] = new_edition
            j.write("volunteer.json", {"volunteer": data})
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == '4':
            print('')
            page_volunteer(volunteer)
            break

        else:
            print('Back to before...')
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please select a valid action.")
            print('')
            edit_volunteer_profile(volunteer)
            break


def create_refugee_profile(volunteer):
    print('')
    print(f'\033[1;36mCurrent refugee profiles:\033[0m')

    a = 1
    for i in utilities.get_information("refugee.json"):
        print(f'[ {a} ] {i}')
        a += 1

    print('')
    print('\033[1;30;47mAction available:\033[0m')
    print('\033[0;35m[ 1 ]\033[0m Create a new refugee profile\n'
          '\033[0;35m[ 2 ]\033[0m Edit refugee profiles\n'
          '\033[0;35m[ 3 ]\033[0m Delete refugee profiles\n'
          '\033[0;35m[ 4 ]\033[0m Back to the welcome page.')
    print('')

    decision = input('Select an ' + '\033[0;34maction\033[0m' ': ')

    while True:
        print('')
        if decision == '1':
            c_data = j.read("refugee.json")["refugee"]
            while True:
                refugee_name = input('\033[0;34mName\033[0m: ')
                if refugee_name not in [*c_data]:
                    break
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please select a valid Name.")
            while True:
                gender = input('\033[0;34mGender\033[0m is (male/female): ')
                if gender == 'male' or gender == 'm' or gender == 'M' or gender == 'Male':
                    refugee_gender = True
                    break
                elif gender == 'female' or gender == 'f' or gender == 'F' or gender == 'Female':
                    refugee_gender = False
                    break
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please enter a valid word.")

            refugee_age = int(input('\033[0;34mAge\033[0m : '))

            refugee_phone = input('\033[0;34mContact number\033[0m : ')

            health_status = {1: "No pain",
                             2: "Mild pain",
                             3: "Moderate pain",
                             4: "Severe pain",
                             5: "Worst pain/EMERGENCY"}

            key_list = [*health_status]  # 把字典的所有的Key转换成一个list
            print('')

            while True:
                health = int(input('The refugee health status list is shown below,\n'
                                   'Please input the number.\n'
                                   '\033[0;35m[ 1 ]\033[0m No pain,\n'
                                   '\033[0;35m[ 2 ]\033[0m Mild pain,\n'
                                   '\033[0;35m[ 3 ]\033[0m Moderate pain,\n'
                                   '\033[0;35m[ 4 ]\033[0m Severe pain,\n'
                                   '\033[0;35m[ 5 ]\033[0m Worst pain/EMERGENCY\n'
                                   'The \033[0;34mhealth status\033[0m is: '))

                if health in key_list:
                    refugee_health = health_status[health]
                    break
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please enter a valid word.")

            print('')
            num_family = int(input('\033[0;34mNumber of family members\033[0m: '))
            family_members = []

            for i in range(num_family):
                family_name = input('The name of family members: ')
                family_members.append(family_name)

            print('')
            # v_data = j.read("volunteer.json")["volunteer"]  # get this vol info
            # e_data = j.read('emergency_plan.json')["emergency_plan"]  # get emergency plan info
            # v_plan = v_data[volunteer.getUserName()][5]  # 存在的 volunteer emergency plan
            # c_data = j.read('camp.json')["camp"]  # camp info
            # camp available
            # if v_plan in [*e_data]:
            #     a_camps = e_data[v_plan][6]  # available camp
            #     print('\033[0;34mDetails of camp\033[0m')
            #     a = 1
            #     for i in a_camps:
            #         print(f'< {a} > {i}')
            #         a += 1
            #         # 从camp.json里查找camp信息
            #         if i in [*c_data]:
            #             print('Camp details: ')
            #             # print(c_data['camp'][i])
            #             camp_info = c_data[i]
            #             print(f'Camp name: {camp_info[0]}\n'
            #                   f'Refugee list: {camp_info[1]}\n'
            #                   f'Camp status: {camp_info[2]}\n'
            #                   f'')

            volunteer.create_refugee_profile(refugee_name, refugee_phone, refugee_gender, refugee_age,
                                             refugee_health, family_members)

            print('\033[1;32mCreate successfully.\033[0m')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == '2':
            print(f'\033[1;36mCurrent refugee profiles:\033[0m')

            a = 1
            for i in utilities.get_information("refugee.json"):
                print(f'[ {a} ] {i}')
                a += 1

            print('')
            data = j.read("refugee.json")["refugee"]
            key_list = [*data]
            while True:
                name = input('Enter the \033[0;34mrefugee name\033[0m you want to edit.\n'
                             'The \033[0;34mrefugee name\033[0m is: ')

                print('')
                if name in key_list:
                    break
                else:
                    print('Please enter a valid name.')
                    # print("please input the correct refugee name")

            detail = data[name]
            r = refugee(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5])
            edit_refugee_details(r, volunteer)
            break

        elif decision == '3':
            del_name = input('\033[0;34mRefugee name delete\033[0m: ')
            # 检查是否在list里
            data = j.read('refugee.json')['refugee']
            for key in data:
                if key == del_name:
                    del data[key]
                    break
            j.write('refugee.json', {"refugee": data})
            print('')
            print('\033[1;32mDelete successfully.\033[0m')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == '4':
            page_volunteer(volunteer)
            break

        else:
            print('')
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please enter a valid word.")
            page_volunteer(volunteer)
            break


def get_all_refugee_details():
    print(f'\033[1;36mCurrent refugee profiles:\033[0m')

    a = 1
    for i in utilities.get_information("refugee.json"):
        print(f'[ {a} ] {i}')
        a += 1

    return


def edit_refugee_details(r, volunteer):
    data = j.read("refugee.json")
    while True:
        decision = input('\033[1;30;47mAction available:\033[0m\n'
                         '\033[0;35m[ 1 ]\033[0m' + ' Name\n'
                         '\033[0;35m[ 2 ]\033[0m' + ' Contact number\n'
                         '\033[0;35m[ 3 ]\033[0m' + ' Health status\n'
                         '\033[0;35m[ 4 ]\033[0m' + ' Camp\n'
                         '\033[0;35m[ 5 ]\033[0m' + ' Family members\n'
                         '\033[0;35m[ 6 ]\033[0m' + ' Back to the welcome page\n'
                         '\n'
                         'Select an ' + '\033[0;34maction\033[0m' ': ')

        print('')
        if decision == "1":
            print('\033[1;30;47mEditing\033[0m')
            data = data["refugee"]
            while True:
                new_name = input('The ' + '\033[0;34mnew name\033[0m is: ')
                if new_name not in [*data]:
                    break
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please select a valid Name.")
            refugee_info = data[r.getName()]
            del data[r.getName()]
            r.setName(new_name)
            refugee_info[0] = new_name
            data[new_name] = refugee_info
            j.write('refugee.json', {"refugee": data})
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == "2":
            print('\033[1;30;47mEditing\033[0m')
            new_information = input('The ' + '\033[0;34mnew contact number\033[0m is: ')
            r.setPhone(new_information)
            data['refugee'][r.getName()][1] = new_information
            j.write('refugee.json', data)
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == "3":
            print('\033[1;30;47mEditing\033[0m')
            while True:
                choice = input('Select the number of information you want to change:\n'
                               '\033[0;35m[ 1 ]\033[0m No pain\n'
                               '\033[0;35m[ 2 ]\033[0m Mild pain\n'
                               '\033[0;35m[ 3 ]\033[0m Moderate pain\n'
                               '\033[0;35m[ 4 ]\033[0m Severe pain\n'
                               '\033[0;35m[ 5 ]\033[0m Worst pain/EMERGENCY\n'
                               '\n'
                               'The health status is: ')

                if choice.isdigit():
                    new_health_status = int(choice)

                    key_list = [*health_status]
                    if new_health_status in key_list:
                        new_information = health_status[new_health_status]
                        r.setStatus(new_health_status)
                        data['refugee'][r.getName()][4] = new_information
                        j.write('refugee.json', data)
                        print('')
                        print('\033[1;32mEdit successfully.\033[0m')
                        print('Back to the welcome page...')
                        print('')
                        page_volunteer(volunteer)
                        break
                    else:
                        print("\033[1;31mInvalid action\033[0m\n"
                              "Please select a valid action.")
                        print('')
                else:
                    print("\033[1;31mInvalid action\033[0m\n"
                          "Please select a valid action.")
                    print('')

        elif decision == "4":
            print('\033[1;30;47mEditing\033[0m')

            print(f'\033[1;36mCurrent available camps:\033[0m')
            v_data = j.read("volunteer.json")["volunteer"]  # get this vol info
            e_data = j.read('emergency_plan.json')["emergency_plan"]  # get emergency plan info
            v_plan = v_data[volunteer.getUserName()][5]  # 存在的volunteer emergency plan
            c_data = j.read('camp.json')["camp"]  # camp info

            # camp available
            if v_plan in [*e_data]:
                # 找到可用的camps
                a_camps = e_data[v_plan][6]  # available camps
                a = 1
                for i in a_camps:
                    print(f'[ {a} ] {i}')
                    a += 1
                    # 从camp.json里查找camp信息
                    if i in [*c_data]:
                        print('Camp details: ')
                        data = c_data[i]
                        print(f'Camp name: {data[0]}\n'
                              f'Refugee list: {data[1]}\n'
                              f'Camp status: {data[2]}\n'
                              f'')
                r_data = j.read("refugee.json")["refugee"]
                # the old camp is
                oldcamp = r_data[r.getName()][6]

                print('\033[0;34mThe current camp is\033[0m: ' + oldcamp)
                print('')

                # the new camp is
                r_camp = input('\033[0;34mNew camp is\033[0m: ')

                if r_camp in a_camps:
                    c_data[oldcamp][1].remove(r.getName())
                    j.write('camp.json', {'camp': c_data})

                    c_data[r_camp][1].append(r.getName())
                    j.write('camp.json', {'camp': c_data})

                    r_data[r.getName()][6] = r_camp
                    j.write('refugee.json', {'refugee': r_data})

                    print('')
                    print('\033[1;32mEdit successfully.\033[0m')
                    print('Back to the welcome page...')
                    print('')
                    page_volunteer(volunteer)
                    break

                else:
                    print("\033[1;31mInvalid camp\033[0m\n"
                          "Please select a valid camp: ")
                    print('')

        elif decision == "5":
            print('\033[1;30;47mEditing\033[0m')
            print("The current families is:")
            r_data = j.read("refugee.json")["refugee"]
            family_list = r_data[r.getName()][5]
            a = 1
            for i in family_list:
                print(f'[ {a} ] {i}')
                a += 1

            new_information = int(input('The ' + '\033[0;34mnew number of family members\033[0m is: '))
            family_members = []

            for i in range(new_information):
                family_name = input('Name of family members: ')
                family_members.append(family_name)

            family = family_list + family_members
            r_data[r.getName()][5] = family
            j.write('refugee.json', {"refugee" : r_data})
            print('')
            print('\033[1;32mEdit successfully.\033[0m')
            print('Back to the welcome page...')
            print('')
            page_volunteer(volunteer)
            break

        elif decision == '6':
            page_volunteer(volunteer)
            break
        else:
            print('')
            print("\033[1;31mInvalid action\033[0m\n"
                  "Please enter a valid word.")
            print('')
    return r

