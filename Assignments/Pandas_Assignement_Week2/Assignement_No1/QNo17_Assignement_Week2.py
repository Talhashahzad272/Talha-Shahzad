import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)

# Selecting a single row using .iloc
# Select 5th row
# , print the returned row and analyze results.

row_5 = df.iloc[4]
print(row_5)