import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# Conditional selection of rows using .loc
# “city” equal to “Adjuntas” and “price” is equal to - less then 180500
# , print the returned row and analyze results.

selecting_price_city = df.loc[(df["city"] == "Adjuntas") & (df["price"] <= 180500)]
print(selecting_price_city)