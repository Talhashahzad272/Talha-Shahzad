import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

'''Selecting a single column using .loc
With index value 7 , only select following columns
“city”,”price” , ”street” , ” zip_code” , ” acre_lot”
, print the returned row and analyze results.'''

multiplecolum = ["city","price","street","zip_code","acre_lot"]
row_7_colum = df.loc[7,multiplecolum]
print(row_7_colum)