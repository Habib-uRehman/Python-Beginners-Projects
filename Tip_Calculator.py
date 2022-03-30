print("Welcome to Tip Calculator")
totalBill = float(input("what was the total bill?"))
percentage = float(input("what percentage would you like to give 10, 12, or 15?"))
splitting = float(input("how many People to split the bill"))

billWithPercent = totalBill + (totalBill * percentage/100)
eachPersonBill = billWithPercent / splitting
print(round(eachPersonBill,2))