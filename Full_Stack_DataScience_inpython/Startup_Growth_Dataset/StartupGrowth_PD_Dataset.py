import pandas as pd

# Load CSV file of StartUp Growth dataset in pandas
df_StartupG = pd.read_csv("Full_Stack_DataScience_inpython\Startup_Growth_Dataset\startup_growth_investment_data.csv", delimiter=",")
print(df_StartupG)

print("df_StartupG - data types" , df_StartupG.info())
print("df_StartupG - data types" , df_StartupG.describe())
print("df_StartupG - data types" , df_StartupG.shape)
print("df_StartupG - data types" , df_StartupG.dtypes)


# display the first Seven rows
print("first Seven rows:",df_StartupG.head(7))

# display the last Seven rows
print("last Seven rows:",df_StartupG.tail(7))

# access the Name column
print("Access the colum Industry:",df_StartupG["Industry"])

# access multiple columns
print("Access the multiple colum:", df_StartupG[["Funding Rounds","Investment Amount (USD)"]])

#Selecting a single row using .loc

print("Access the single row:", df_StartupG.loc[4])

#Selecting multiple rows using .loc
print("#Selecting multiple rows using .loc", df_StartupG.loc[[3,6,5]])

#Selecting a slice of rows using .loc
print("#Selecting a slice of rows using .loc:", df_StartupG.loc[8:20])

#Conditional selection of rows using .loc
print(df_StartupG.loc[df_StartupG["Industry"] == "E-commerce"])

# Silicing of Rows with a single colum using .loc
print(df_StartupG.loc[1:20, "Funding Rounds"])

# Silicing of Rows with a multiple colum using .loc
print(df_StartupG.loc[1:20, ["Funding Rounds", "Valuation (USD)"]])

# Sciling of rows and colum using .loc
print(df_StartupG.loc[2:7, "Startup Name": "Investment Amount (USD)"])

#Combined row and column selection using .loc
print(df_StartupG.loc[df_StartupG["Industry"] == "EdTech", "Startup Name":"Investment Amount (USD)"])

# Case 2 : using .loc with index_col - starts here
df_StartupG_col = pd.read_csv("Full_Stack_DataScience_inpython\Startup_Growth_Dataset\startup_growth_investment_data.csv", delimiter=",", index_col="Startup Name")
print(df_StartupG_col)

print("df_StartupG - data types" , df_StartupG_col.info())
print("df_StartupG - data types" , df_StartupG_col.describe())
print("df_StartupG - data types" , df_StartupG_col.shape)

#Selecting a single row using .loc
print(df_StartupG_col.loc["Startup_8"])

#Selecting multiple rows using .loc
print(df_StartupG_col.loc[["Startup_8","Startup_10"]])

#Selecting a slice of rows using .loc
print(df_StartupG_col.loc["Startup_1":"Startup_8"])

#Conditional selection of rows using .loc
print(df_StartupG.loc[df_StartupG["Industry"] == "E-commerce"])

#Selecting a single column using .loc
print(df_StartupG_col.loc["Startup_1":"Startup_8", "Funding Rounds" ])

#Selecting multiple columns using .loc
print(df_StartupG_col.loc["Startup_1":"Startup_8", ["Funding Rounds","Valuation (USD)" ]])

#Selecting a slice of columns using .loc
print(df_StartupG_col.loc["Startup_1":"Startup_8", "Funding Rounds" : "Valuation (USD)" ])


#Combined row and column selection using .loc
print(df_StartupG.loc[df_StartupG["Industry"] == "EdTech", "Startup Name":"Investment Amount (USD)"])

#Selecting a single row using .iloc
print("#Selecting a single row using .iloc",df_StartupG_col.iloc[5])

#Selecting a multiple row using .iloc
print("#Selecting a multiple row using .iloc",df_StartupG_col.iloc[[5,6,7]])

#Selecting a slicing row using .iloc
print("#Selecting a multiple row using .iloc",df_StartupG_col.iloc[4:22])

#Selecting a slicing row using .iloc and select a single colum
print("#Selecting a multiple row using .iloc",df_StartupG_col.iloc[4:22,3])

#Selecting a slicing row using .iloc and select a multiple colum
print("#Selecting a multiple row using .iloc",df_StartupG_col.iloc[4:22,[3,4,5,6]])

#Selecting a slicing row using .iloc and sciling of colum
print("#Selecting a multiple row using .iloc",df_StartupG_col.iloc[4:22,0:4])

#Add a New Row to a Pandas DataFrame
df_StartupG_col.loc[len(df_StartupG_col.index)] = ["Startup_5000","EdTech",10,3309031930.22,15482697353.099028,39,"Singapore",2016,190.47]
print(df_StartupG_col)

#Remove Rows/Columns from a Pandas DataFrame

# delete row with index 1
df_StartupG_col.drop( 1, axis = 0, inplace = True)   #Method 1
df_StartupG_col.drop( index = 2 , inplace = True)   #Method 2

# delete rows with index 3 and 5
df_StartupG_col.drop(index= [3,5] , inplace = True)

# delete one column
df_StartupG_col.drop('Funding Rounds', axis=1, inplace=True)
print(df_StartupG_col)
# delete multiple colums 
df_StartupG_col.drop(columns=["Startup Name","Funding Rounds"], inplace=True)
print(df_StartupG_col)


#Rename Labels in a DataFrame
# Rename first colum 
df_StartupG_col.rename(columns={"Startup Name":"Startup_Name_change"},inplace=True)

# Rename Multiple colum 
df_StartupG_col.rename(mapper={"Startup Name":"Startup_Name_change","Funding Rounds":"Funding_Rounds_Change"},inplace=True)

#  Rename Row Labels
print(df_StartupG.rename(index={3:4}, inplace=True))

# Rename multiple rows
print(df_StartupG_col.rename(mapper={2:5,6:7}, inplace=True))


# select the rows where the Funding Rounds id greater then 7
queery_df =df_StartupG_col.query("Funding Rounds" == 7 or "Funding Rounds" > 7)
print(queery_df)

# sort DataFrame by Year Founded in ascending order
sorted_df = df_StartupG_col.sort_values(by='Year Founded')
print(sorted_df.to_string(index=False))

# 1. Sort DataFrame by 'Year Founded' and then by 'Funding Rounds' (Both in ascending order)
df1 = df_StartupG_col.sort_values(by=['Year Foundede', 'Funding Rounds'])

print("Sorting by 'Year Founded' (ascending) and then by 'Funding Rounds' (ascending):\n")
print(df1.to_string(index=False))

# group the DataFrame by the Investment Amount (USD) column and
# calculate the sum of Valuation (USD) for each category

grouped = df_StartupG_col.groupby("Investment Amount (USD)")["Valuation (USD)"].sum()
print(grouped.to_string())
print(len(grouped))

""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values
df_cleaned = df_StartupG_col.dropna()
print("Cleaned Data:\n",df_cleaned)

# filling NaN values with 0
df_StartupG_col.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df_StartupG_col)

# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)

# creating a pandas.array of integers
int_array = pd.array((data), dtype=int)
print(int_array)




