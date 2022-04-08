# Pizza Calculator
print("Welcome to PiZZa Delivery App")
size = input("Please Enter Which size of Pizza You want: S | L | M: \n")
pepperoni = input("Do you Want Pepperoni? Y | N")
extraCheese = input(" Do you Want Extra Cheese? Y | N")
bill = 0

if size == "S":
    bill = 15
    print("you order Small pizza")
    if pepperoni == "Y":
        bill = bill + 2
        print("and Pepperoni")
elif size == "M":
    bill = 20
    print("You ordered Mediam Pizza")
    if pepperoni == "Y":
        bill = bill + 3
        print("and Pepperoni")
elif size == "L":
    bill = 25
    print("you ordered Large Pizza")
    if pepperoni == "Y":
        bill = bill + 3
        print("and Pepperoni")
if extraCheese == "Y":
    bill+=1
    print(f"Your Order Bill is ${bill}")
else:
    print(f"Your Order Bill is ${bill}")
