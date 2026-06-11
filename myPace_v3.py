totalpace = 0

for person in range(5):
    myTimeMin = int(input("Time in min = "))
    while myTimeMin <= 0:
        myTimeMin = int(input("Time in min = "))
    myTimeSec = myTimeMin*60
    print("my time in seconds =",myTimeSec)

    myDistanceKm = int(input("distance = "))
    while myDistanceKm <= 0:
        myDistanceKm = int(input("distance = "))
    myDistanceMiles = myDistanceKm/1.61
    print("my distance in miles =", myDistanceMiles)

    pace1 = myTimeMin/myDistanceKm
    pace2 = myTimeSec/myDistanceMiles

    if pace1 < 5:
        print("Wow, you are an athlete!")
    elif  5 <= pace1 < 6:
        print("This is excellent!!")
    elif 6 <= pace1 < 7:
        print("Your pace is very good!")
    else:
        print("Good job!")

    totalpace += pace1

    print("my pace min/km =",pace1)
    print("my pace sec/miles =",pace2)

print("The average pace (min/km) was",totalpace/5)

