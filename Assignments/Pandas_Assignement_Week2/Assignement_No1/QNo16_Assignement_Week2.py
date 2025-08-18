import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# Combined row and column selection using .loc
# “city” equal to “Adjuntas” and Form “city” to “zip_code”
# , print the returned row and analyze results.

combine_row_colum = df.loc[df["city"] == "Adjuntas", "city":"zip_code"]
print(combine_row_colum)