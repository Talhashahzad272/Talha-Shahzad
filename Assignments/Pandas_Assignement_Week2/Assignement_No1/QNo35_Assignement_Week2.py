import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)


# use dropna() to remove rows with any missing values
# Print the returned dataFrame and analyze results.

remove_misingValues = df.dropna()
print(remove_misingValues)