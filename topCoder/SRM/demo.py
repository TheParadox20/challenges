possiblePoints = []
for i in range(1,4):
    for j in range(1,21):
        if (possiblePoints.count(i*j)>0):
            #print()
            continue
        possiblePoints.append(i*j)
possiblePoints.append(25)
possiblePoints.append(50)
possiblePoints.sort()
print((possiblePoints[42]))
print(len(possiblePoints))