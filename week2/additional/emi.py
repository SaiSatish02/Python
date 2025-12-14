import math
princ_amt = float(input("Enter principal amount: "))
rate = float(input("Enter monthly rate of interest: "))
num_pay=int(input("Enter number of months: "))

emi = (princ_amt * rate * (math.pow(1 + rate, num_pay))) / (math.pow(1 + rate, num_pay) - 1)
print("EMI is:", round(emi,2))