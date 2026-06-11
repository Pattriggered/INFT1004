excellent = 0
good = 0
average = 0
poor = 0

excellentTips = 0
goodTips = 0
averageTips = 0
poorTips = 0

totalTips = 0
totalServices = 0

service = input("How was your service? Excellent/Good/Average/Poor: ").lower()

while service != "end":

    mealPrice = float(input("How much was the meal? "))

    if service == "excellent":
        tip = mealPrice * 0.15
        excellent += 1
        excellentTips += tip

    elif service == "good":
        tip = mealPrice * 0.10
        good += 1
        goodTips += tip

    elif service == "average":
        tip = mealPrice * 0.05
        average += 1
        averageTips += tip

    elif service == "poor":
        tip = 0
        poor += 1
        poorTips += tip

    else:
        print("Invalid input")
        service = input("How was your service? Excellent/Good/Average/Poor: ").lower()
        

    totalTips += tip
    totalServices += 1

    print("You tipped $", tip)

    service = input("How was your service? Excellent/Good/Average/Poor: ").lower()

print("\nSummary")
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)

if excellent > 0:
    print("Average excellent tip =", excellentTips / excellent)

if good > 0:
    print("Average good tip =", goodTips / good)

if average > 0:
    print("Average average tip =", averageTips / average)

if poor > 0:
    print("Average poor tip =", poorTips / poor)

if totalServices > 0:
    print("Average tip of all services =", totalTips / totalServices)