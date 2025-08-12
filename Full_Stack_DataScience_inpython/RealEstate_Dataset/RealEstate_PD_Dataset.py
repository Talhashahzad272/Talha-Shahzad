import pandas as pd

# Data load in data_frame of "RealEstate_USA"

df_RealEstate = pd.read_csv("Full_Stack_DataScience_inpython\RealEstate_Dataset\RealEstate-USA.csv",delimiter=",")

print(df_RealEstate)                                                               # print data of RealEstate_USA in pandas


print("Data_types (RealEstate_USA):",df_RealEstate.dtypes)                         # print data_type RealEstate_USA Data

print("Shape (RealEstate_USA):",df_RealEstate.shape)                               # print shape RealEstate_USA Data

print("info of (RealEstate_USA) ", df_RealEstate.info())                           # print info RealEstate_USA Data

print("Describe function of (RealEstate_USA) ", df_RealEstate.describe())          # print describe function RealEstate_USA Data

print("First Five rows (RealEstate_USA):", df_RealEstate.head())                                    # print first five rows of RealEstate_USA Data

print("Last Five rows (RealEstate_USA):", df_RealEstate.tail())                                     # print first five rows of RealEstate_USA Data

print("First Seven rows (RealEstate_USA):", df_RealEstate.head(7))                                  # print first Seven rows of RealEstate_USA Data

print("Last Nine rows (RealEstate_USA):", df_RealEstate.tail(9))                                    # print last nine rows of RealEstate_USA Data

print("Colum name (house_size)", df_RealEstate["house_size"])                                       # print the single colum with name (house_size)

print("Multiple colum Access with name:", df_RealEstate[["bed","bath"]])                            # Access the multiple colum with name (bed), (bath)
print("Multiple colum Access with name:", df_RealEstate[["bed","bath","price"]])                    # Access the multiple colum with name (bed), (bath),(price)

print("Single row print using loc" ,df_RealEstate.loc[6])                                           # Access the single row using loc indexer
print("Multiple row print using loc" ,df_RealEstate.loc[[0,1,3,6]])                                   # Access the Multiple row using loc indexer

print("sciling of rows:", df_RealEstate.loc[:9])                                                    #Selecting the sciling of rows using of .loc indexer
print("sciling of rows:", df_RealEstate.loc[1:6])                                                    #Selecting the sciling of rows using of .loc indexer

# Conditional selection rows through .loc
print(df_RealEstate)
street_Adjuntas= df_RealEstate.loc[df_RealEstate["city"] == "Ponce" ]
print("Rows print only Adjuntas (Street) colum: ", street_Adjuntas)

# Using a sciling for Selecting a single column using .loc

print("Using sciling for a single colum:", df_RealEstate.loc[0:2,"price"])                           #For price
print("Using sciling for a single colum:", df_RealEstate.loc[0:2,"street"])                          #For street

# Using a sciling for Selecting a Multiple column using .loc

print("Using sciling for a Multiple colum:", df_RealEstate.loc[0:2,["price","state"]])                           #For price and state
print("Using sciling for a Multiple colum:", df_RealEstate.loc[0:5,["street","zip_code"]])                       #For street and zip_code

#Selecting a slice of columns using .loc

print("Using sciling for a Multiple colum:", df_RealEstate.loc[0:2,"price":"state"])                           #For price and state
print("Using sciling for a Multiple colum:", df_RealEstate.loc[0:5,"street":"zip_code"])                       #For street and zip_code

#Combined row and column selection using .loc

print("Using rows and colum:", df_RealEstate.loc[df_RealEstate["city"] == "Adjuntas", "price":"state"])
  

#   Case eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee2

df_index_col = pd.read_csv("Full_Stack_DataScience_inpython\RealEstate_Dataset\RealEstate-USA.csv",delimiter=",")
print(df_index_col)

print("Data_types (RealEstate_USA):",df_index_col.dtypes)                         # print data_type RealEstate_USA Data

print("Shape (RealEstate_USA):",df_index_col.shape)                               # print shape RealEstate_USA Data

print("info of (RealEstate_USA) ", df_index_col.info())                           # print info RealEstate_USA Data
print("describe of (RealEstate_USA) ", df_index_col.describe())                   # print info RealEstate_USA Data

#Selecting a single row using .loc
print("Select a single row using loc:", df_index_col.loc[5])

#Selecting multiple rows using .loc
print("Select a single row using loc:", df_index_col.loc[[0,7]])

#Selecting a slice of rows using .loc
print("Sciling of rows using .loc:", df_index_col.loc[:8])

#Conditional selection of rows using .loc
street_Adjuntas= df_RealEstate.loc[df_RealEstate["city"] == "Ponce" ]
print("Rows print only Adjuntas (Street) colum: ", street_Adjuntas)

print("Using sciling for a Multiple colum:", df_RealEstate.loc[3:7,"price":"state"])                           #For price and state
print("Using sciling for a Multiple colum:", df_RealEstate.loc[2:4,"street":"zip_code"])                       #For street and zip_code

print("Using rows and colum:", df_RealEstate.loc[df_RealEstate["city"] == "Adjuntas", "price":"state"])

# Case 3 : Using .iloc - starts here
#Selecting a single row using .iloc

print("Selecting a single row using .iloc:", df_index_col.iloc[0])

#Selecting multiple rows using .iloc
print("Selecting a multiple row using .iloc:", df_index_col.iloc[[0,4,5]])

#Selecting a slice of rows using .iloc
print("slicing of row using .iloc:", df_index_col.iloc[0:3])

#Selecting a single column using .iloc
print("Selecting a single colum using .iloc:", df_index_col.iloc[0:3,3])

#Selecting multiple columns using .iloc
print("Selecting a multiple colum using .iloc:", df_index_col.iloc[0:3,[1,2,3]])

#Selecting a slice of columns using .iloc
print("Slicing of colum using .iloc:", df_index_col.iloc[:,2:6])

#Combined row and column selection using .iloc
print("combition of rows and colum:", df_index_col.iloc[[1,3,4,5],3:7])

#Add a New Row to a Pandas DataFrame
df_index_col.loc[len(df_index_col.index)] = [2343,"for sale",52343,6,3,0.34,1404990,"Juana Diaz","Puerto Rico",795,748,352]
print(df_index_col)
print()

#Remove Rows/Columns from a Pandas DataFrame 
# delete row with index 1
df_index_col.drop(1,axis=0,inplace=True)   #Method 1 for delete of row
df_index_col.drop(index=2,inplace=True)   #Method 2 for delete of row
print(df_index_col)
# Delete multiple rows 
df_index_col.drop(index=[3,10],axis=0, inplace=True)
print("Delete rows [1,2,3]:",df_index_col)

#Rename Labels in a DataFrame
df_index_col.rename(columns={"status" : "status_change"}, inplace=True)
print(df_index_col)
# Multiple colum name change
df_index_col.rename(mapper={"bed":"bed_change","bath":"bath_change"}, inplace=True)
print(df_index_col)
#  Rename Row Labels
df_index_col.rename(index={5:7}, inplace=True)
# Multiple rows change with another rows
df_index_col.rename(mapper={8:9,4:6},inplace=True)
print(df_index_col)

#query() to Select Data
Selcted_rows = df_index_col.query("bed == 4 and bath == 2")
print(Selcted_rows.to_string())

# sort DataFrame by price in ascending order

sorted_Values = df_index_col.sort_values(by="price")
print(sorted_Values.to_string(index=False))

#Pandas groupby
Group_by =df_index_col.groupby("state")["price"].sum()
print(Group_by)
print("lenth of grouped by:", len(Group_by))

# use dropna() to remove rows with any missing values

df_cleand = df_index_col.dropna()
print(df_cleand)
# filling NaN values with 0

filling_values = df_index_col.fillna(0,inplace=True)
print(filling_values)
# create a list named data
array1= pd.array(df_index_col)
print(array1)

# creating a pandas.array of integers
int_array1 = pd.array(df_index_col,dtype="int")
print(int_array1)

