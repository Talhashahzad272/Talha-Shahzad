import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)

# Selecting a slice of columns using .iloc
# Range: Select from 2nd column to 5th columns
# , print the returned row and analyze results.

colum_range = df.iloc[:,2:5]
print(colum_range)
