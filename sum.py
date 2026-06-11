
s = 0
i = (input("Please enter a positive number or else (quit): "))
while i != "quit":
    num = int(i)
    s += num
    i = (input("Please enter a positive number: "))
print(s)

