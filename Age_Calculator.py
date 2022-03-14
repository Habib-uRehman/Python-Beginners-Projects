# Challenge 3 day 2: Age Calculator.


totalWeaks = 90 * 52
totalDays = 90 * 365
totalMonths = 90 * 12
age = int(input("what is your current age? \n"))
returnWeaks = age * 52
returnDays = age * 365
returnMonths = age * 12

weeks = totalWeaks - returnWeaks
days = totalDays - returnDays
months = totalMonths - returnMonths
print(f"you have left with {months} months, {days} Days, and {weeks} Weeks")
