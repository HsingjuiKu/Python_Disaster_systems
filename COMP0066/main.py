import admin
import camp
import refugee
import volunteer
from tkinter import *
import admin_page as ap
import volunteer_page as vp
import login


# try:
#     vp.volunteer_profile(volunteer.volunteer("volunteer1", 111, "zhangsan", 111, True, "shanghai",))
# except Exception:
#     print("A Exception occur")
# else:
#     print("没有发生报错时候执行的代码")
# finally:
#     print("不管什么情况都会执行的代码")

def role_choice():
    while True:
        try:
            print('')
            print("\033[1;30;47mRole Selection\033[0m")
            print("Log in as " + "\033[4;34mAdmin (A/a)\033[0m" + " or " + "\033[4;34mVolunteer (V/v)\033[0m" + ' ?')
            role = input("Your " + "\033[4;34mrole\033[0m" + " is: ")
            print("Welcome to the humanitarian emergency management system.")
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

        except (Exception):
            print("A Exception occur...")


role_choice()
