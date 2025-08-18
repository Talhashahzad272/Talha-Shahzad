import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# Rename column “state” to “state_Changed”
# Print the returned dataFrame and analyze results.

df.rename(columns={"state":"state_Changed"},inplace=True)
print(df)

df.rename(mapper={"city":"city_change"},axis=1,inplace=True)
print(df)