HD = 0
D = 0
C = 0
P = 0
F = 0
student = 0
mark = 0
result = 0

studentNo = int(input("please select a student number (-1 to end)"))
while studentNo != -1 :
    valid = False
    while not valid:
        test1 = int(input("How much did you get for the first test? (Max 25)"))
        if 0 <= test1 <= 25:
            valid = True
        else:
            print("Please enter a mark between 0 and 25")

    valid = False
    while not valid:
        test2 = int(input("How much did you get for the second test? (Max 25)"))
        if 0 <= test2 <= 25:
            valid = True
        else:
            print("Please enter a mark between 0 and 25")

    valid = False
    while not valid:
        test3 = int(input("How much did you get for the final test? (Max 50)"))
        if 0 <= test3 <= 50:
            valid = True
        else:
            print("Please enter a mark between 0 and 50")

    if test3 < 25:
        print("You failed the main exam and did not pass")
        F += 1
    else:
        result = test1 + test2 + test3

        if result >= 85:
            print("High Distinction")
            HD += 1
        elif result >= 75:
            print("Distinction")
            D += 1
        elif result >= 65:
            print("Credit")
            C += 1
        elif result >= 50:
            print("Pass")
            P += 1
        else:
            print("Fail")
            F += 1
    student += 1
    mark += result
    studentNo = int(input("please select a student number (-1 to end)"))

averageMark = mark/student
print("the number of HD's are: ",HD)
print("the number of D's are: ",D)
print("the number of C's are: ",C)
print("the number of P's are: ",P)
print("the number of F's are: ",F)
print("the total number of students is ",student, "and the average mark of all students is ",averageMark)