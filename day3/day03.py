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
    #print(listList)

#create empty list, as long as one of the inputs (12)
gammaList = [None] * len(listList[0])

for i in range(0, len(listList[0])):
    for j in range(0, len(listList)):
        ans = ExtractElement(listList, i)
        count0 = 0
        count1 = 0
        for k in range(0, len(ans)):
            if ans[k] == "0":
                count0 += 1
            else:
                count1 += 1
        if count1 > count0:
            gammaList[i] = "1"
        else:
            gammaList[i] = "0"
        

print(gammaList)
#epsilon list is just reverse of gamma list
epsilonList = [None] * len(gammaList)
for i in range(0, len(gammaList)):
    if gammaList[i] == "0":
        epsilonList[i] = "1"
    else:
        epsilonList[i] = "0"

print(epsilonList)

#now convert gamma and epsilon from lists with strings to binary
gammaString = "".join(gammaList)
gammaRate = int(gammaString, 2)
print(gammaRate)
epsilonString = "".join(epsilonList)
epsilonRate = int(epsilonString, 2)
print(epsilonRate)

print("answer = ", gammaRate*epsilonRate)