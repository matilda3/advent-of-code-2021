def column(matrix, i):
    return [row[i] for row in matrix]

with open("day4\input.txt") as f:
    values = f.readlines()

#make list of int bingo numbers
bingoNrs = (values.pop(0).rstrip()).split(",")
for i in range(0, len(bingoNrs)):
    bingoNrs[i] = int(bingoNrs[i])

#split values into bingo boards

#remove all the empty lines and chunk into fives
values = [value for value in values if value != "\n"]
values = [values[i:i + 5] for i in range(0, len(values), 5)]
#make the boards into further lists of rows, also int
for boards in range(0, len(values)):
    for rows in range(0, len(values[boards])):
        values[boards][rows] = values[boards][rows].strip().split()

winningNumber = 0
winningBoard = []
#call out all numbers
for i in range(0, 15):
    number = bingoNrs[i]
    print("number: ", number)
    #go through and mark off all of that number
    for boards in range(0, len(values)):
        for rows in range(0, len(values[boards])):
            for numbers in range(0, len(values[boards][rows])):
                #print(values[boards][rows][numbers])
                if(values[boards][rows][numbers] == number):
                    #mark off as *
                    print("match: *")
                    values[boards][rows][numbers] = "*"
    #check for a winner
    #go through all rows
    for boards in range(0, len(values)):
        for rows in range(0, len(values[boards])):
            #check if all elements in a row are the same
            if(len(set(values[boards][rows])) == 1):
                #bingo
                print("bingo")
                winningNumber = number
                winningBoard = values[boards]
                break
    #go through all columns
    for boards in range(0, len(values)):
        for i in range(0, len(values[boards][rows])):
            c = column(values[boards], i)
            if(len(set(c)) == 1):
                #bingo
                print("bingo")
                winningNumber = number
                winningBoard = values[boards]
                break

#print(values)