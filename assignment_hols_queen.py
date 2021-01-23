# from the finance file deduce month by month the difference in income. Determine the monthly income, change in income, 
#and the month with the highest and lowest income.
#steps to take.
#1. Loop through all transactions
# 2. Check date on each transaction
# check amount on each transaction
# 4. convert month from numeric to text value
#5. Dump value in dictionary

import datetime

file_name = "financials.csv"

file= open(file_name, "r") #OPEN FILE IN READ MODE

data= file.readlines() #READ FILE LINES

data.pop(0) #REMOVE THE FIRDT LINE WHICH IS THE HEADER
month_names = ["January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December",
]
result_dict= dict.fromkeys(month_names, 0)

#result_dict = {} #empty dictionary to contain the values on collection

#THIS PART ONLY RECORDS THE FINAL VALUES FOR EACH MONTH BECAUSE IT REPLACES THE OLD VALUES EVERYTIME

# for transaction in data: #LOOP THROGH ALL TANSACTIONS

#     split_transaction = transaction.split(",") #split individual transactions in individual values
#     #convert string date to python date object
#     date = datetime.datetime.strptime(split_transaction[3], "%d/%m/%Y")
#     month_name= date.strftime("%B") #get actual month name in text format
    
#     transaction_amount= split_transaction[6]
#     transaction_amount_as_number= float(transaction_amount) #convert transaction amount to decimal number
#     #print(transaction_amount)


#     result_dict[month_name] = transaction_amount_as_number # APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME
#     print(result_dict)

for transaction in data: #LOOP THROGH ALL TANSACTIONS

    split_transaction = transaction.split(",") #split individual transactions in individual values
    #convert string date to python date object
    date = datetime.datetime.strptime(split_transaction[3], "%d/%m/%Y")
    month_name= date.strftime("%B") #get actual month name in text format
    # print(month_name)
    
    transaction_amount= split_transaction[6]
    transaction_amount_as_number= float(transaction_amount) #convert transaction amount to decimal number
    #print(transaction_amount)

    if month_name in result_dict.keys():
        result_dict[month_name] += transaction_amount_as_number # APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME
        
    else:
        result_dict[month_name] = transaction_amount_as_number 

#print(result_dict)

#GET HEIGHEST AND LOWEST MONTHS TRANSACTION

#print(result_dict.items())
values_list = list(result_dict.items())
print(values_list)
values_list.sort(key=lambda  val: val[1])
print(values_list[0]) #LOWEST MONTH
print(values_list[-1]) #HIGHEST MONTH

# #GET MONTHLY DIFFERENCE
# previous_month_name= "non"
# previous_month_amount = 0

# for month, amount in result_dict.items():
#     print(month, amount)
#     print(previous_month_name, month, amount-previous_month_amount)
#     previous_month_name = month
#     previous_month_amount = amount
# go thorugh each tansaction
#check company name
#write it into afile with company name

file_name = "C:/Users/Queen Adiat/Desktop/UNIVELCITY COURSE/PROGRAMS/financials.csv"

file= open(file_name, "r") #OPEN FILE IN READ MODE

data= file.readlines() #READ FILE LINES

data.pop(0) #REMOVE THE FIRDT LINE WHICH IS THE HEADER

destination_path ="C:/Users/Queen Adiat/Desktop/UNIVELCITY COURSE/PROGRAMS/company data"

for transaction in data: #LOOP THROGH ALL TANSACTIONS

    split_transaction = transaction.split(",") #split individual transaction in indivisual values
    company_name=split_transaction[5]
#print(split_transactions)

    company_file= open (f"{destination_path}/{company_name.replace('/', '-')}.csv" , "a")
    company_file.write(transaction)
    company_file.close()