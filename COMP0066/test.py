import js as j
import utilities
from admin import admin
import datetime
import volunteer
import admin_page as ap
import volunteer_page as vp
import refugee


# path = "account.json"
# print(path[:-5:])
# a = admin('zhangsan',111, True, 20, 'zhangsan', 111)2

# a.create_emergency_plan('suzhou', 'dizhen', 'die', 'huadong')
# # print(datetime.datetime.now().isoformat())
# a = input("please input number")
# a = int(a)
# print("that is: "+ a)
# print(f'Here is the current plan below:\n{utilities.get_information("account.json")}')


# admin = admin('zhangsan', 111, True, 20, 'admin', 111)
# admin.create_Volunteer("volunteer4","111","zhaoliu","110",True,"London",True)

# ap.page_admin()
# vp.page_volunteer("Volunteer3", "111", "wangwu" , "119", True, "London", True)
# r = refugee.refugee("zhangsan", "120",True, 12, "health", "london")
# r.setName("wangwu")
# r.setPhone("134")
# print(r.name, r.phone)
#

utilities.generate_report('big wind')
