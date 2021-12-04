from types import CoroutineType


def ExtractElement(list, num):
    return[item[num] for item in list]

values = []
#open and read text file
with open('day3\day03(input).txt') as f:
    values = f.readlines()

#list of lists
listList = []

#for each input, turn it into a list, and stick that list into the list of lists
for i in range(0, len(values)):
    #values[i] is a string, turn it into a list
    list = [c for c in values[i]]
    #remove last element
    list.pop()
    #add list to list of lists
    listList.append(list)

print(len(listList))

copyList = listList

#need to go through each position in each list to determine what number is most/least common in each position
position = 0
while len(listList) > 1:
    bit = []
    count0 = 0
    count1 = 0
    if len(listList) == 1:
        #print("there is only one left now")
        break
    for num in listList:
        if num[position] == "0":
            count0 += 1
        else:
            count1 += 1
    if count0 < count1:
        #most common value is 1: 1 is >= 0
        #print("mcv = 1")
        mcv = "1"
    elif count0 == count1:
        mcv = "1"
        #print("mcv = 1")
    else:
        mcv = "0"
        #print("mcv = 0")
    temp = []
    for num in listList:
        if num[position] == mcv:
            temp.append(num)
            #print("temp ", temp)
    listList = temp
    position += 1

#oxygen generator rating
print(listList[0])
#to decimal
ogr = int("".join(listList[0]), 2)
print("ogr: ", ogr)

#need to do everything again for lcv
#print(copyList)
position2 = 0
while len(copyList) > 1:
    bit = []
    count0 = 0
    count1 = 0
    if len(copyList) == 1:
        #print("there is only one left now")
        break
    for num in copyList:
        if num[position2] == "0":
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        #lcv is 1: that means
        #print("lcv = 1")
        lcv = "1"
    elif count0 == count1:
        lcv = "0"
        #print("lcv = 0")
    else:
        lcv = "0"
        #print("lcv = 0")
    temp = []
    for num in copyList:
        if num[position2] == lcv:
            temp.append(num)
            #print("temp ", temp)
    copyList = temp
    position2 += 1
#CO2 scrubber rating
print(copyList[0])
co2r = int("".join(copyList[0]), 2)
print("co2r: ", co2r)

lsr = ogr * co2r
print("lsr: ", lsr)