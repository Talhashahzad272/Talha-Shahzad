import numpy as np

# Load the CSV File of FastFoodResturant in mumpy

address,city,country,latitude,longitude = np.genfromtxt("Full_Stack_DataScience_inpython\FastFoodResturant_Dataset\FastFoodRestaurants.csv", delimiter=",",usecols=(0,1,2,4,5),unpack=True,dtype=None,invalid_raise=False, skip_header=1)

print(address)
print(city)
print(country)
print(latitude)
print(longitude)



# FastFood_Resturant - statistics operations
print("FastFood_Resturant (latitude) mean: " , np.mean(latitude))
print("FastFood_Resturant (latitude) Average: " , np.average(latitude))
print("FastFood_Resturant (latitude) Std: " , np.std(latitude))
print("FastFood_Resturant (latitude) Median: " , np.median(latitude))
print("FastFood_Resturant (latitude) Percentile_25: " , np.percentile(latitude,25))
print("FastFood_Resturant (latitude) Percentile_50: " , np.percentile(latitude,50))
print("FastFood_Resturant (latitude) Percentile_75: " , np.percentile(latitude,75))
print("FastFood_Resturant (latitude) Min: " , np.min(latitude))
print("FastFood_Resturant (latitude) Max: " , np.max(latitude))

# FastFood_Resturant - maths operations
print("FastFood_Resturant (latitude) square: " , np.square(latitude))
print("FastFood_Resturant (latitude) sqrt: " , np.sqrt(latitude))
print("FastFood_Resturant (latitude) pow: " , np.power(latitude,latitude))
print("FastFood_Resturant (latitude) abs: " , np.abs(latitude))

# FastFood_Resturant - arithmatic operations

addition = latitude + longitude
subtraction = latitude - longitude
multiplication = latitude * longitude
division = latitude / longitude

print("FastFood_Resturant Addition: " , addition)
print("FastFood_Resturant Substraction: " , subtraction)
print("FastFood_Resturant Multiplication: " , multiplication)
print("FastFood_Resturant Division : " , division )

#Trigonometric Functions
latitudePie = (latitude/np.pi) +1


# Calculate the natural logarithm and base-10 logarithm
sine_values = np.sin(latitudePie)
cosine_values = np.cos(latitudePie)
tangent_values = np.tan(latitudePie)

print("FastFood_Resturant Sin  : " , sine_values)
print("FastFood_Resturant Cos  : " , cosine_values)
print("FastFood_Resturant Tan  : " , tangent_values)

print("FastFood_Resturant Exponential values:", np.exp(latitudePie))

# Calculate the natural logarithm and base-10 logarithm

log_array = np.log(latitudePie)
log10_array = np.log10(latitudePie)

print("FastFood_Resturant - Natural logarithm values:", log_array)
print("FastFood_Resturant = Base-10 logarithm values:", log10_array)

# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(latitudePie)
print("FastFood_Resturant  - Hyperbolic Sine values:", sinh_values)
cosh_values = np.cosh(latitudePie)
print("FastFood_Resturant  - Hyperbolic cos values:", cosh_values)
tanh_values = np.tanh(latitudePie)
print("FastFood_Resturant  - Hyperbolic tan values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(latitudePie)
print("FastFood_Resturant  -Inverse Hyperbolic Sine values:", asinh_values)
acosh_values = np.arccosh(latitudePie)
print("FastFood_Resturant  -Inverse Hyperbolic cos values:", acosh_values)
atanh_values = np.arctanh(latitudePie)
print("FastFood_Resturant  -Inverse Hyperbolic tan values:", atanh_values)

#FastFood_Resturant  Long Plus Lat - 2 dimentional arrary
D2LongLat = np.array([latitude,longitude])

print ("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - data type" ,D2LongLat.dtype) 

# Splicing array
D2LongLatSlice=  D2LongLat[:1,:5]
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2LongLatSlice)
D2LongLatSlice2=  D2LongLat[:1, 4:15:4]
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2LongLatSlice2)

# Indexing array
D2LongLatSliceItemOnly=  D2LongLatSlice[0,1]
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2LongLatSliceItemOnly)
D2LongLatSlice2ItemOnly=  D2LongLatSlice2[0, 2]
print("FastFood_Resturant Long Plus Lat - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2LongLatSlice2ItemOnly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2LongLat):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongLat[0])[0]
cols = np.shape(D2LongLat[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongLat[i,j])
"""


# 2 x 149 ========>>>>> 1  x 298 - reshape
D2LongLat1TO298 = np.reshape(D2LongLat, (1, 298))
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : " , D2LongLat1TO298)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : Size " , D2LongLat1TO298.size)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2LongLat1TO298.ndim)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : shape " , D2LongLat1TO298.shape)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2LongLat1TO298.ndim)




print()




















