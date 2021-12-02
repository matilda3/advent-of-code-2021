#create empty list for values in text file
values = []
#open and read text file
with open('day01(input).txt') as f:
    values = f.readlines()
#set counter for increased to 0
increased = 0
prevList = []
for i in range(0, 3):
    prevList.append(int(values[i]))

for i in range(0, len(values)):
    num = int(values[i])
    list = []
    if((i + 3) > (len(values))):
        break
    for j in range(i, (i + 3)):
        list.append(int(values[j]))
    #print(list)
    #print("prev: ", prevList)
    if(sum(list) > sum(prevList)):
        increased += 1
        #print("increased: ", increased)
    prevList = list
print(increased)