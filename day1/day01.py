#create empty list for values in text file
values = []
#open and read text file
with open('day01(input).txt') as f:
    values = f.readlines()
#set counter for increased to 0
increased = 0
#start with the previous number as the first number
previousNum = int(values[0])
#go through all the numbers in the list
for i in range(0, len(values)):
    #turn into int from str
    values[i] = int(values[i])
    #print("previous: ", previousNum)
    #print("current num: ", values[i])
    if(values[i] > previousNum):
        increased += 1
        #print("increased")
        #print("numbers that have increased: ", increased)
    previousNum = values[i]
    #print("new previous number: ", previousNum)
print("total: ", increased)