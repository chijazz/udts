# word = "conquuistadore"
# traget ="q"

# for i in word:

#     if i == target:
#         print(f"Found letter {traget}.")
#         break
#     else:
#         print ("Not Found")

# target = "Mr"
# staffs = ("Mr Ali", "Master")

#LOOP CLASSWORK

# # import the time module 
# import time 

# # define the countdown func. 
# def countdown(t): 
	
# 	while t: 
# 		mins, secs = divmod(t, 60) 
# 		timer = '{:02d}:{:02d}'.format(mins, secs) 
# 		print(timer, end="\r") 
# 		time.sleep(1) 
# 		t -= 1
	
# 	print('Fire in the hole!!') 


# # input time in seconds 
# t = input("Enter the time in seconds: ") 

# # function call 
# countdown(int(t)) 

# import time
# min = 2
# start = 30
# end = 0
# interval = -1

# while True:
#     min += interval

#     while True:
#         start += interval
#         print(min, "mins : ", start, "secs")
#         time.sleep(1)

#         if start == end:
#             break


# import time
# import winsound

# seconds = int(input("Enter your start time in seconds : "))

# hours = seconds//(60*60)
# mins = (seconds//60)%60 # 0 if temp_mins < 0 else temp_mins #TENARY OPERATOR
# seconds = seconds % 60

# end = 0
# interval = -1

# while True:
#     while True:
#         while True:

#             if seconds == end:
#                 break
            
#             seconds += interval 
#             print (hours, "hours : ", mins, "mins :", seconds, "secs")
#             time.sleep(0.1)

#         seconds = 60
#         if mins == end:
#             break

#         mins += interval

#     mins = 60
#     if hours == end:
#         break
#     hours += interval

# winsound.Beep(1000, 500)
# time.sleep(1)
# winsound.Beep(1000, 500)
# time.sleep(1)
# winsound.Beep(1000, 500)
# time.sleep(1)
# winsound.Beep(1000, 500)
# time.sleep(1)


# word = "I am a boy"
# for i in range()
# for i in enumerate(word):
#     print(i)

# for index, i in enumerate(word):
#     print(index, "-", i)

# import time
# for i in range(60):
#     for j in range(60):
#         for k in range(60):
#             print(i,"hour", j, "mins", k, "seconds")
#             time.sleep(0.001)

# import time
# for i in reversed(range(60)):
#     for j in reversed(range(60)):
#         for k in reversed(range(60)):
#             print(i,"hour", j, "mins", k, "seconds")
#             time.sleep(0.001)

# import time

# seconds = int(input("Please input number of seconds here : "))

# hours = seconds//(60*60)
# mins = (seconds//60)%60
# seconds = seconds%60

# for i in reversed(range(hours+1)):
#     for j in reversed(range(mins+1)):
#         for k in reversed(range(seconds+1)):
#             print(i,"hour", j, "mins", k, "seconds")
#             time.sleep(0.001)


import time

seconds = int(input("Please input number of seconds here : "))

hours = seconds//(60*60)
mins = (seconds//60)%60
seconds = seconds%60

for i in reversed(range(hours+1)):
    for j in reversed(range(mins+1)):
        for k in reversed(range(seconds+1)):
            print(i,"hour", j, "mins", k, "seconds", end="")
            time.sleep(1)
            print("\r", end="")
        seconds = 60
    mins = 60

