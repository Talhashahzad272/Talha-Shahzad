import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# group the DataFrame by the “city” column and calculate the sum of “price” for each category
# Print the returned dataFrame and analyze results

grouped = df.groupby("city")["price"].sum()
print(grouped.to_string())
print(len(grouped))