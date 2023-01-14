from volunteer import volunteer
import utilities
import numpy as np
import admin_page as ap
import volunteer_page as vp
import volunteer as v
import js as j
# Admin Login


def admin_login():
    print('')
    print('\033[1;30;47mWelcome to the Admin Login System\033[0m')
    account_book = j.read("account.json")["account"]
    while True:
        admin_username = input("\033[0;34mUsername\033[0m" + ": ")
        admin_password = input("\033[0;34mPassword\033[0m" + ": ")

        if admin_username in [*account_book]:
            if admin_username == "admin":
                if admin_password == account_book[admin_username]:
                    print('')
                    print("\033[1;32mYou have successfully logged in. \033[0m")
                    print('')
                    ap.page_admin()
                    break
                else:
                    print('')
                    print("\033[1;31mWrong Password, please try again. \033[0m")
                    print('')
            else:
                print('')
                print("\033[1;31mThis is not admin account, Please re-choose! \033[0m")
                print('')
        else:
            print('')
            print("\033[1;31mInvalid Username, please try again. \033[0m")
            print('')


# Volunteer Login


def vol_login():
    print('\033[1;30;47mWelcome to the Volunteer Login System\033[0m')

    account_book = j.read('account.json')["account"]
    while True:
        vol_username = input("\033[0;34mUsername\033[0m" + ": ")
        vol_password = input("\033[0;34mPassword\033[0m" + ": ")

        if vol_username in [*account_book]:
            if vol_username != "admin":
                if account_book[vol_username] == vol_password:
                    find_volunteer = j.read("volunteer.json")["volunteer"][vol_username]

                    volunteer = find_volunteer[6]

                    if volunteer is True:
                        print('')
                        print("\033[1;32mYou have successfully logged in. \033[0m")
                        print('')
                        find_volunteer = j.read("volunteer.json")["volunteer"][vol_username]

                        volunteer = v.volunteer(find_volunteer[0],
                                                find_volunteer[1],
                                                find_volunteer[2],
                                                find_volunteer[3],
                                                find_volunteer[4],
                                                find_volunteer[5],
                                                find_volunteer[6])

                        vp.page_volunteer(volunteer)
                        break

                    else:
                        print('')
                        print("\033[1;31mSorry, your account is deactivated. \033[0m")
                        print('')
                else:
                    print('')
                    print("\033[1;31mWrong Password, please try again. \033[0m")
                    print('')
            else:
                print('')
                print("\033[1;31mInvalid Username, please try again. \033[0m")
                print('')
        else:
            print('')
            print("\033[1;31mInvalid Username, please try again. \033[0m")
            print('')
            