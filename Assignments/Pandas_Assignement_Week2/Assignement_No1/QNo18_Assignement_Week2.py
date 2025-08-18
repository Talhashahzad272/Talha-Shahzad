import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)

# Selecting multiple rows using .iloc
# Select – 7
# th row, 9th row and 15th row
# , print the returned row and analyze results

row_multiselect = df.iloc[[7,9,15]]
print(row_multiselect)