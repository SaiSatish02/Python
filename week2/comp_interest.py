princ_amt=float(input("Enter principal amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time in years: "))
compd_amt=princ_amt*((1+rate/100)**time)
compd_interest=compd_amt - princ_amt
print("Compound Interest is:", compd_interest)
