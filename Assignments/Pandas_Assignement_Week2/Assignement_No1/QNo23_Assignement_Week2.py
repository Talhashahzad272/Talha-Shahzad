import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)

# Combined row and column selection using .iloc
# Select – 
# th row, 9th row and 15th row
# Select 2nd column, 4th column
# , print the returned row and analyze results.

row_colum_combine = df.iloc[[9,15],[2,4]]

print(row_colum_combine)