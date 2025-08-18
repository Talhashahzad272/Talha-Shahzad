import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)


# delete row with index 2
# print the returned dataFrame and analyze results.

row_del = df.drop(index=1,inplace=True)
print(row_del)
print(df)
