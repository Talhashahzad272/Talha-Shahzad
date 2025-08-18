import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)


# Selecting multiple columns using .iloc
# Select 2nd column, 4th column, 7th columns
# , print the returned row and analyze results.

colm_multiple = df.iloc[:,[2,4,7]]
print(colm_multiple)

