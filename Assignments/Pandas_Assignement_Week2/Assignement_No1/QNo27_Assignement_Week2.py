import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# delete row with index from 4 to 7th row
# print the returned dataFrame and analyze results

row_delet_range = df.drop(index=range(4,7),axis=0,inplace=True)
print(row_delet_range)
print(df)