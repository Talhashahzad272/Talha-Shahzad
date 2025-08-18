Basic_Sal = float(input("Enter Here Basic_Salary:\n"))
print(f"Basic_Salary is: {Basic_Sal}")
HRA =(20/100)*Basic_Sal
print(f"Percentage of HRA:{HRA}")
DA =(15/100)*Basic_Sal
print(f"Percentage of HRA:{DA}")
Total_Salary = Basic_Sal + HRA + DA
print(f"Total_Salary is:{Total_Salary}")