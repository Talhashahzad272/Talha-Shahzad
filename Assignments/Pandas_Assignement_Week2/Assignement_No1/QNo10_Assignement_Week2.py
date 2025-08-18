import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# print multiple row with slicing using .loc print [3to9]

scling_multiple_row = df.loc[3:9]
print(scling_multiple_row)