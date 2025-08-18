import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)
# Conditional selection of rows using .loc
# “city” equal to “Adjuntas”
# , print the returned row and analyze results.

selectingrow_city_Adjuntas = df.loc[df["city"] == "Adjuntas"]

print(selectingrow_city_Adjuntas)