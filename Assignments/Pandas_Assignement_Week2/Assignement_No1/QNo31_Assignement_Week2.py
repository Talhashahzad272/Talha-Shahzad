import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)


# Rename label from 3 to 5
# Print the returned dataFrame and analyze results.

df.rename(columns={3:5},inplace=True)
print(df)


