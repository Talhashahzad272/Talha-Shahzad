import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)

'''Combined row and column selection using .iloc
Select range : 2
nd
 row, 6
th row
Select range : 2
nd column to 4
th column
, print the returned row and analyze results.'''

row_colm_seleing = df.iloc[2:6,2:4]
print(row_colm_seleing)