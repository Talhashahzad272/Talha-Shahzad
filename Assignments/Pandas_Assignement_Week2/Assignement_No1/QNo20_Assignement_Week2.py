import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",", index_col="house_size")

# print all data of Real Estate in datafaram

print(df)


# Selecting a single column using .iloc
# Select 3rd column
# , print the returned row and analyze results

colm_select = df.iloc[:,3]
print(colm_select)