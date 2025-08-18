import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)


# sort DataFrame by price in ascending order column “price”

sort_colum_price = df.sort_values(by="price")
print(sort_colum_price.to_string(index=False))