import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# Selting a single row using [.loc] base on indexing "5"
 
row_5 = df.loc[4]

print(row_5)
