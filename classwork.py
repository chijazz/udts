# Write a program to take in "name and age", Print out year of birth; print out if your were born after 1989 (True or False)

name = input("Enter your name: ")
age = float(input("Enter your age: "))
current_year = 2020
year_of_birth = (current_year - age)

print("If you were born after the year 1989 : ", year_of_birth>1989)
