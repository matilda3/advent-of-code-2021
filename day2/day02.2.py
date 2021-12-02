values = []
with open('day02(input).txt') as f:
    values = f.readlines()

positionX = 0
depth = 0
aim = 0

for i in range(0, len(values)):
    intake = values[i].split()
    if(intake[0] == "forward"):
        positionX += int(intake[1])
        depth += (aim * int(intake[1]))
        #print("X+ ", int(intake[1]))
        #print("depth + ", depth)
    elif(intake[0] == "up"):
        aim -= int(intake[1])
        #print("aim - ", int(intake[1]))
    elif(intake[0] == "down"):
        aim += int(intake[1])
        #print("aim + ", int(intake[1]))
    else:
        break

print("x: ", positionX)
print("y: ", depth)
print("aim: ", aim)
print(positionX * depth)