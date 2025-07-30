import pandas as pd

df = pd.read_csv('Full_Stack_DataScience_inpython\FastFoodResturant_Dataset\FastFoodRestaurants.csv',delimiter=",")

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column
city = df['city']
print("access the Name column: df : ")
print(city)
print()

# access multiple columns
city_name = df[['city','name']]
print("access multiple columns: df : ")
print(city_name)
print()

#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()


#Conditional selection of rows using .loc
second_row4 = df.loc[df['city'] == 'Massena']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:1,['city','name']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'name':'city']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Massena','city':'name']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col - starts here

df_index_col = pd.read_csv('Week2/zameencom-property-data-By-Kaggle-short.csv',delimiter=";" , index_col='address')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


#Selecting a single row using .loc
second_row = df_index_col.loc["324 Main St"]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[["324 Main St", "1111 New Pointe Blvd"]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc["324 Main St":"1111 New Pointe Blvd"]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Massena','city':'name']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:"324 Main St",'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:"324 Main St",['city','name']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:"324 Main St",'city':'name']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['city'] == 'Massena','city':'name']
print("#Combined row and column selection using .loc")
print(second_row8)


# Case 3 : Using .iloc - starts here


#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

df.loc[len(df.index)] = ["125 Towne Center Dr","Lexington","US","us/ky/lexington/125townecenterdr/-1055723171",38.06753,-84.53043,"Domino's Pizza",40511,"KY","https://www.dominos.com/en/?redirect=homepageandutm_source=locallistingsandutm_medium=loclistandutm_campaign=localmaps,https://www.dominos.com/en/?redirect=homepage,https://www.dominos.com/en/?redirect=homepageandutm_source=yextandutm_medium=loclistandutm_campaign=localmaps"] 
print("Modified DataFrame - add a new row:")
print(df)
print()

#Remove Rows/Columns from a Pandas DataFrame


# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)

# delete age column
df.drop('city', axis=1, inplace=True)
# delete marital status column
df.drop(columns='city', inplace=True)
# delete height and profession columns
df.drop(['name', 'city'], axis=1, inplace=True)

# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='address')
print(sorted_df.to_string(index=False))
























