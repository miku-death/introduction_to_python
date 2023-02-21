cranes = int(input())

if(cranes % 2 != 0) print("неверное S")
else:
    sergeCranes = cranes / 4
    peterCranes = cranes / 4
    kateCranes = cranes / 2

    print(sergeCranes, peterCranes, kateCranes) 
