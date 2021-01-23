# Using the ope() and for loop; create a program to write 2 times table into a file (x.csv)

num = int("2")  
# using for loop to iterate multiplication 10 times 
# 
with open("c:/Users/VALUEMEDIA ADMIN/Desktop/Univelcity DTS/multi_table.csv", "w")   as file:
    for i in range(1,11):  
        print(num,'x',i,'=',num*i) 
        file.write(f"{num},'x',{i},'=',{num*i}\n") 

# import csv
# with open("c:/Users/VALUEMEDIA ADMIN/Desktop/Univelcity DTS/multi_table.csv", "r")