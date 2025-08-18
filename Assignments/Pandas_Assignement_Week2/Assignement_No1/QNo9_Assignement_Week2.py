import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# print multiple row 3,5 and 7 using .loc

multiple_row = df.loc[[3,5,7]]
print(multiple_row)