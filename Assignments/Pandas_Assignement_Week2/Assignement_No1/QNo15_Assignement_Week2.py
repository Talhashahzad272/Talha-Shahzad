import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

'''Selecting a slice of columns using .loc
Form “city” to “zip_code”
, print the returned row and analyze results.'''

sciling_multiplecolum = df.loc[:,"city":"zip_code"]
print(sciling_multiplecolum)