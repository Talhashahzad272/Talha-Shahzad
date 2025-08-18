import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# Print first Seven Rows of Real Estate Data

print("First Seven Rows of Real Estate data:", df.head(7))