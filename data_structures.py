# oloture_sub = open("Oloture.2019.WEBRip.x264-FGT-English.srt", "r")
# counter = 0

# # print(oloture_sub.read())

# for line in oloture_sub.readlines():

#     if "forze speciali" in line.lower():
#         print("found - ", line)



oloture_sub = open("Oloture.2019.WEBRip.x264-FGT-English.srt", "r")
counter = 1

# print(oloture_sub.read())

for line in oloture_sub.readlines():

    if "forze speciali" in line.lower():
        print("found in line - ", counter, " - ", line)

    counter += 1
print(counter) 