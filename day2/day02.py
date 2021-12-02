values = []
with open('day02(input).txt') as f:
    values = f.readlines()

positionX = 0
positionY = 0

for i in range(0, len(values)):
    intake = values[i].split()
    if(intake[0] == "forward"):
        positionX += int(intake[1])
        #print("X+ ", int(intake[1]))
    elif(intake[0] == "up"):
        positionY -= int(intake[1])
        #print("Y+ ", int(intake[1]))
    elif(intake[0] == "down"):
        positionY += int(intake[1])
        #print("Y- ", int(intake[1]))
    else:
        break

print("x: ", positionX)
print("y: ", positionY)
print(positionX * positionY)