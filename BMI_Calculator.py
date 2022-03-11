# BMI Calculator
weight = float(input("enter your weight: \n"))
height = float(input("Enter your Height in meters\n "))

bmi = weight / height ** 2
if bmi <= 18.5:
    print("underWeight")
elif bmi > 18.5 or bmi < 24.9:
    print("Normal")
elif bmi >= 25 or bmi < 29.9:
    print("overWeight")
else:
    print("Obese")
