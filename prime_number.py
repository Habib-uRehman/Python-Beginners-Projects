# Prime Number Checker

def prime_checker(number):
    isprime = True
    for n in range (2,number):
        if number % n == 0:
           isprime = False
    if isprime == True:
        print(f"{number} is Prime number")
    else:
        print(f"{number} is not Prime number")

nu = int(input("Enter Number"))
prime_checker(nu)
