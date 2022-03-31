# # Day 3 Leap Year Calculator

year = int(input("Enter a year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("leap year")
else:
    print("Not Leap Year")