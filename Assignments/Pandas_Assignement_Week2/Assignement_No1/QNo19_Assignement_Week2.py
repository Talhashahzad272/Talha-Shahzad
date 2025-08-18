import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)

# Selecting a slice of rows using .iloc
# Select from 5th to 13th row
# , print the returned row and analyze results.

row_selec = df.iloc[5:13]
print(row_selec)