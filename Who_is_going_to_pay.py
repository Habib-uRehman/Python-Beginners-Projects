# WHO IS GOING TO PAY CHALLANGE IN LISTS day 4

import random
inputs = input("Enter Names Separated by , and space; \n")  # inputs = "khan, lala, sab, jan"

names = inputs.split(", ")
size = len(names)
random_number = random.randint(0,size)
print(f"{names[random_number]} will pay today\n")
print(f"Bill of {names}")