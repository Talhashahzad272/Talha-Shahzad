import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df.to_string())

# query() to Select Data
# where: "price” < 127400
# “city” not equal to “Adjuntas”
# Print the returned dataFrame and analyze results

selected_rows = df.query("city == \'Adjuntas\' or price < 127400")
print(selected_rows.to_string())
print(len(selected_rows))