# # THIS CLASS IS BASICALLY FOR DATA STRUCTURES

# ### LISTS -  COMMA SEPAREATED VALUES INSIDE SQUARE BRACES.

# fruits = ["apples", "potatoes", "yams"]

# print(fruits)
# print("variable fruits is of type -: ", type(fruits))


# ### ADD TO THE FRUITS LIST USING APPEND

# fruit_to_add = "fish"

# print("BEFORE APPENDING")
# print(fruits)

# fruits.append(fruit_to_add)
# print("##AFTER APPENDING")
# print(fruits)


# ### REMOVE THE FRUITS LIST USING REMOVE METHOD

# print()
# print("##AFTER APPENDING")
# fruits.remove("yams")
# print(fruits)

# ### COUNT NUMBER OF ITEMS IN LIST USING .COUNT METHOD

# print()
# print("##AFTER COUNT")
# fruits.append("apples")
# number_of_times_apples_occures_in_list = fruits.count ("apples")
# print("Apple occurs : ", number_of_times_apples_occures_in_list)

# ### EXTEND MY LIST USING .EXTEND METHOD
# print()
# print("##AFTER EXTENDING")
# fruits.extend(["monkey"])
# # extend_list = fruits.extend(["monkey"])
# print(fruits)

# # ### INSERT INTO MY LIST USING .INSERT METHOD
# # print()
# # print("##AFTER INSERTING")
# # fruits.insert("vamps")
# # insert_list = fruits.insert("vamps")
# # print(fruits)

# ### INDEXING LIST

# print(fruits[1])

# fruits.append(["1, 2, 3, 4"])
# print(fruits)

# for i in range(4):
#     print(fruits[0], "- at position ", i)


# ### USING A WHILE LOOP, DO THE ABOVE THINGY
# print(fruits[1])

# fruits.append(["1, 2, 3, 4"])
# print(fruits)

# i = 0
# while i < 4:
#     print(fruits[0], "- at position ", i)
#     i += 1


# ### SLICING LIST
# print()
# data_list = ["ali", "benky", "sule", 2, 3, 12, 14, True, False, True, False]

# strings = data_list[0:3]
# numbers = data_list[3:7]
# booleans = data_list[8:11]
# jumping_steps = data_list[0:12:2]  #start stop step
# slice_out_becky_3 = data_list[1:5]

# print("Strings List -->", strings)
# print("Numebr list -->", numbers)
# print("Booleans list -->", booleans)
# print("jumping list -->", jumping_steps)
# print("slice_out_example -->", slice_out_becky_3)

# # i = 0
# # while i < 4:
# #     print(slice_out_becky_3[i], i)
# #     i += 1

# i = 0
# while i < len(data_list):
#     print(data_list[i], i)
#     i += 1


financials = open("financials.csv", "r")

# print(financials.readline()[12:20]) #GET TAX TYPE VIA SLICING 

# headling_list = financials.readline().split(",")

# print(headling_list)
# print(headling_list[5])

# for line in financials.readlines():
#     print(line.split(",")[7])

# cash_transactions = []

# for line in financials.readlines():
#     transactions_type = line.split(",")[7]

#     if transactions_type== "Own Bank Che...":
#         print(line.split(",")[5], line.split(",")[8])


# ### ASSINGMENT 
# OF UNIQUE COMPANIES IN THE FILE AND HOW MUCH THEY PAID IN TAX EACH AND PLACE IN A DICTIONARY

# for line in financials.readlines():
#     unique_company = line.split(",")[5]
    
# # def unique_company(company):
# #     list_of_unique_company = []
# #     unique_company = set(company)

# #     for company in unique_company:
# #         list_of_unique_company.append(unique_company)

# #     return list_of_unique_company

#     print(unique_company)
#     unique_company = set(company)
#     list_of_unique_company = unique_company.append(unique_company)
#     print(list_of_unique_company)


financials = open("financials.csv", "r")
companies = []
def unique_companies (file):
    """Take a file as input and return a set of unique companies"""
    for line in financials.readlines():
        if "company" not in line:
            companies.append(line.split(",")[5])
            financials.seek(0)
    unique_companies = set(companies)
    return unique_companies
print(unique_companies(financials))

counter = 1

for line in financials.readlines():

    if "unique_companies" in line.lower():
        unique_companies = set(unique_companies(financials))
        print("unique_companies(financials) - ", counter, " - ", line)

    counter += 1
print(counter) 
