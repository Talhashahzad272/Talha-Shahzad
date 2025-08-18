import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

'''Conditional selection of rows using .loc
“price” greater then “100000”
, print the returned row and analyze results.'''

seletingrow_price = df.loc[df["price"] >= 100000]

print(seletingrow_price)