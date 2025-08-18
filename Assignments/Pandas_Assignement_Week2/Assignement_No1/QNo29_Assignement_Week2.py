import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

#  Delete “house_size” and “state” columns
# print the returned dataFrame and analyze results

df.drop(["house_size","state"],axis=1,inplace=True)
print(df)
