# Write a program (module) that will perform the following;
# if given set f numbers: e.g., 1,5,3 program will print the mean, variance and Standard
# deviation of numbers.
# Write into a file, the value of x|x_xbar|x_xbar_squared

# O D V
# O D V           Using python what are the values of (O D V) 
# O D V
# ------
# V V V
# ------

# Write a code that will find three numbers when added using it format then it will give you the last
# set of number. there's built in function that will help.
# hint xyz = zzz
# xyz
# xyz
# xyz
# ----
# zzz
# -----




# DO COLLECTION OF VALUES JUST ONCE
# value = input("Please enter values to input : ")
# value_to_integer = int(value)

# print(value_to_integer)

# # DO COLLECTION OF VALUES OVER AND OVER
# values_list = []
# while True:
#     value = input("Please enter values to input : ")
#     value_to_integer = float(value)

# print(value_to_integer)

# DO COLLECTION OF VALUES JUST OVER AND OVER THEN CREATE A LIST WITH COLLECTED NUMBERS
# values_list = []
# while True:
#     value = input("Please enter values to input : ")
#     value_to_integer = float(value)

#     values_list.append(value_to_integer)
#     print(values_list)


# DO COLLECTION OF VALUES JUST OVER AND OVER THEN CREATE A LIST WITH COLLECTED NUMBERS AND ADD A STOP POINT
# import math

# values_list = []
# while True:
#     value = input("Please enter values to input : ")
#     if value.lower() == "q":
#         break

#     value_to_integer = float(value)
#     values_list.append(value_to_integer)
#     print("\nNumbers collected : ", len(values_list), "\n")
# print(values_list)
# number_of_samples = len(values_list)

# mean_of_numbers = sum(values_list)/len(values_list)
# print("MEAN : ", mean_of_numbers)

# x_xbar_map = map(lambda sample: round(sample-mean_of_numbers, 2), values_list)
# x_xbar_values = list(x_xbar_map)
# print("\nX_XBAR : ", x_xbar_values)

# x_xbar_squared_map = map(lambda sample: round(sample**2), x_xbar_values)
# x_xbar_squared_values = list(x_xbar_squared_map)
# print("\nX_XBAR_SQUARED : \n", x_xbar_squared_values)

# variance = math.sqrt(sum(x_xbar_squared_values)/(number_of_samples - 1))
# rounded_variance = round(variance, 2)

# print("\nVARIANCE : \n", rounded_variance)

# file = open("assignment.csv", "w")
# file.write("VALUE, X_XBAR, X_XBAR_SQUARED\n")

# print(f"{'VALUES'.center(6)} | {('X_XBAR').center(6)} | {('X_XBAR_SQUARED').center(6)}")
# print("-"*24)

# for i in range(number_of_samples):

#     print(f"{str(values_list[i]).center(6)} | {str(x_xbar_squared_values[i]).center(6)} | {str(rounded_variance).center(6)}")

#     file.write(f"{values_list[i]} | {x_xbar_values[i]} | {x_xbar_squared_values}\n")



for i in range(100, 999):
    number_multiplied_by_three = i*3
    last_digit = str(i)[2]*3

    print(i, number_multiplied_by_three, last_digit, number_multiplied_by_three == last_digit)

    if number_multiplied_by_three == int(last_digit):
        break

