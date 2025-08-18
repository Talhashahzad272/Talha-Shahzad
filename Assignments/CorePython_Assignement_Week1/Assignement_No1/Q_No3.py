P = float(input("Enter your price:\n"))
print(f"Your Price is:{P}")
R = 10
T = float(input("Enter Your Time Period:\n"))
print(f"Set Timeperiod:{T}")
Campoundintrest = P*(1+R/100)**T-P
print(f":{Campoundintrest}")