import pandas as pd

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# print information of Real Estate Data
print("Info of Real Estate Data:", df.info())

# print Detype of Real Estate Data
print("Detypes of Real Estate Data:", df.dtypes)

# print Describe of Real Estate Data
print("Describe of Real Estate Data:", df.describe())

# print Shape of Real Estate Data
print("Shape of Real Estate Data:", df.shape)