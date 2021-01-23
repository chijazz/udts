# Assignment####
# from the finance file, I want us to deduce month by month, the difference(inc or dec) in income
# Determine the monthly income, then the monthly chnage in income and determine the month with the highest and lowest income 
# Write each company data into diff excel sheets

# Using the Agile Method
# use dictionaries as the most efficient 
# key : value
# using the month (key) : Amount (value)

# 1 Loop through all transactions
# 2 check date of each transactions (check corresponding month)
# 3 check amount of each transactions
# 4 convert month from numeric to text Value
# 5 dump value in a dictionary 

import datetime

file_name = "financials.csv"
file = open(file_name, "r") #OPEN FILE IN READ MODE

data = file.readlines() #READ FILE LINES
data.pop(0) #REMOVES THE FIRST LINE WHICH IS THE HEADER

month_names = ["January ",
        "February ",
        "March ",
        "April ",
        "May ",
        "June ",
        "July ",
        "August ",
        "September ",
        "October ",
        "November ",
        "December ",]


result_dict = {} #EMPTY DICTIONARY TO CONTAIN  THE VALUES ON COLLECTION
       ###THIS PART ONLY RECORDS THE FINAL VALUE FOR EACH MONTH BECAUSE IT REPLACES THE OLD VALUES EVERYTIME.

# for transactions in data: #LOOP THROUGH ALL THE TRANSACTIONS
#     split_transaction = transactions.split(",") # split individual transaction in individual values

#     date = datetime.datetime.strptime(split_transaction[3], "%M/%d/%Y")
#     month_name = date.strftime("%B") #GET ACTUAL MONTH NAME IN TEXT FORMAT
#     #print(month_name)

#     transaction_amount = split_transaction[6]
#     transaction_amount_as_number = float(transaction_amount) #CONVERT TRANSACTION AMOUNT TO DECIMAL NUMBER
#     #print(transaction_amount)

#     result_dict[month_name] = transaction_amount #APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH VALUE
# print(result_dict)


for transactions in data: #LOOP THROUGH ALL THE TRANSACTIONS
    split_transaction = transactions.split(",") # split individual transaction in individual values

    date = datetime.datetime.strptime(split_transaction[3], "%m/%d/%Y")
    month_name = date.strftime("%B") #GET ACTUAL MONTH NAME IN TEXT FORMAT
    #print(month_name)

    transaction_amount = split_transaction[6]
    transaction_amount_as_number = float(transaction_amount) #CONVERT TRANSACTION AMOUNT TO DECIMAL NUMBER
    # print(transaction_amount)

    if month_name in result_dict.keys():
        result_dict[month_name] += transaction_amount_as_number #APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME

    else:
        result_dict[month_name] = transaction_amount_as_number #APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH VALUE
# print(result_dict)

#GET HIGHEST AND LOWEST MONTHS TRANSACTIONS
# print(result_dict.items())

values_list = list(result_dict.items())
# print(values_list)

values_list.sort(key=lambda val: val[1])
# print(values_list[0]) #LOWEST MONTH
# print(values_list[-1]) #HIGHEST MONTH

result_dict = dict.fromkeys(month_names, 0)
print(result_dict)

#GET MONTHLY DIFFERENCE
previous_month_name = "non"
previous_month_value = 0

for month, amount  in result_dict.items():
    # print(month, amount)
    
    # print(previous_month_name, month, amount - previous_month_am)
    # previous_month_name = month
    # previous_month_amount = amount


    file_name = "financials.csv"
    file = open(file_name, "r") #OPEN FILE IN READ MODE

data = file.readlines() #READ FILE LINES
data.pop(0) #REMOVES THE FIRST LINE WHICH IS THE HEADER

destination_path = "C:/Users/VALUEMEDIA ADMIN/Desktop/Univelcity DTS/company data"

for transaction in data: #LOOP THROUGH ALL THE TRANSACTIONS

    split_transactions = transaction.split(",") #split individual transactions in individual values

    company_name = split_transaction [5]
    print(split_transaction[5])

    # company_file = open(f"{destination_path}/{company_name.replace('/', '-')}.csv", "a")
    # company_file.write(transaction)
    # company_file.close()
    