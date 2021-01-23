# # ### ASSINGMENT 
# # OF UNIQUE COMPANIES IN THE FILE AND HOW MUCH THEY PAID IN TAX EACH AND PLACE IN A DICTIONARY

# file = open("financials.csv", "r")
# file_lines = file.readlines()
# file_lines.pop(0)

# cash_transactions = []

# target_company = "CHI LIMITED"
# total = 0


# for line in file_lines:

#     company_name = line.split(",")[5]
#     amount_paid = float(line.split(",")[6])

#     if company_name == target_company:

#         total += amount_paid
#         print(line.split(",")[5], line.split(",")[8])

# print(target_company, " : \nTotal ==> ", total)


# file.close()

# #### GET UNIQUE COMPANY NAMES ########

# all_company_names = []

# for line in file_lines:

#     comapany_name = line.split(",")[5]
#     all_company_names.append(comapany_name)

# my_list = all_company_names
# my_set = set(my_list)
# print(my_set)

# cash_transactions = []

# target_company = "CHI LIMITED"
# total = 0

# amount_paid_by_company = []
# amount_paid_by_companies = []

# for target_company in my_set:

#     total = 0
#     for line in file_lines:

#         company_name = line.split(",")[5]
#         amount_paid = float(line.split(",")[6])

#         if company_name == target_company:

#             total += amount_paid

#     #print(target_company, " : \nTotal ==> ", total)
    
#     amount_paid_by_companies.append([target_company, total])
# amount_paid_by_companies.sort(key = lambda amount: amount[1], reverse = True)
# print(amount_paid_by_companies[:10])
    
# amount_paid_by_companies.append()



# ####################DICTIONARIES##########################
# CREATING DICTIONARIES

# # DIRECT CREATION

# my_dict = {
#     "john":["singing", "dancing"],
#     "ali":["jumping", "dancing"],
#     "simbi":["ten ten", "eating"]
# }

# print(my_dict)

# scores = {
#     "math" : 90,
#     "english" : 77,
#     "physics" : 68
# }

# print(scores)

# test_dict = {
#     "happy" : ["tomison on other days"],
#     "sad" : ["tomison today"]
# }
# print(test_dict)


#ANOTHER FORM

# names = ["samlue", "lucas", "mary"]
# age = [34,21,19]

# print (list(zip(names, age)))

# my_dict = dict() #empty dictionaries can be created using the dict builtin function

# new_dict = dict (zip(names, age))) #dictionaries can also be created using a list of list or list of tuples
# print(new_dict)

# print(my_dict)
# print(list(enumerate(names)))

##### UPDATING DICTIONARIES

# print(my_dict)

# my_dict["laptops"] = ["hp", "acer", "dell", "toshiba"]
# my_dict["phones"] = ["apple", "samsung", "nokia"]
# my_dict["sneakers"] = ["nike air", "jordans", "jeezy's"]
# my_dict[12] = "INVALID ..OOPS...!!!!!"

# print(my_dict)  

# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#UPDATING DICTIONARY VALUES



import datetime
# print(datetime.date.today())
# print(datetime.datetime.now())

time_now = datetime.datetime.now()

print("day :", time_now.day, "Day name :", time_now.strftime("%A"))
print("month :", time_now.month)
print("year :", time_now.year)
print("hour :", time_now.hour)
print("minute :", time_now.minute)
print("second :", time_now.second)
print("micro :", time_now.microsecond)

print(time_now.strftime("%A"))
print(time_now.strftime("%b %d, %Y, %I:%M%p"))

sample_date = "20202012"
print(datetime.datetime.strptime(sample_date, "%Y%d%m").strftime("%b %d, %Y, %I:%M%p"))

import pprint

bio_dict = dict ()

for i in range(10):

    name = input("Please type your adorable name here :")
    age = input("Please enter your age :")
    small_talk = input("Please enter a small talk :")

    time_created = datetime.datetime.now().strftime("%b %d, %Y, %I:%M%p")

    print(name,age)
    print(small_talk)
    print("created at : ", time_created)


    bio_dict[name] = {
        "age": age,
        "small talk": small_talk,
        "time_created": time_created
    }
    action = input("Please do you want to add another ?? y/n :")
    if action == "n":
        break
pprint.pprint(bio_dict)


while True:

    name = input("Please type your adorable name here :")
    age = input("Please enter your age :")
    small_talk = input("Please enter a small talk :")

    time_created = datetime.datetime.now().strftime("%b %d, %Y, %I:%M%p")

    print(name,age)
    print(small_talk)
    print("created at : ", time_created)


    bio_dict[name] = {
        "age": age,
        "small talk": small_talk,
        "time_created": time_created
    }
    action = input("Please do you want to add another ?? y/n :")
    if action == "n":
        break
pprint.pprint(bio_dict)
