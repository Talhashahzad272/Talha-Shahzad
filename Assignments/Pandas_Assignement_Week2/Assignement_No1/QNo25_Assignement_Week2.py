import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

'''Add a new Row to a Pandas DataFrame
 print the returned dataFrame and analyze results'''

df.loc[len(df.index)] = [34.43,234434,"sale",3423434,34.4,3.4,0.354,3245445,"ponce","rico",2343,"Nan"]
print(df)
