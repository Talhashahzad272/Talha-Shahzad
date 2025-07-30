import numpy as np

#CSV file of RealEstate_USA Dataset convert in numpy.....

brokered_by,price,bed,bath,house_size = np.genfromtxt("Full_Stack_DataScience_inpython\RealEstate_Dataset\RealEstate-USA.csv",delimiter=",",usecols=(0,2,3,4,10),unpack=True, dtype=None,skip_header=1)

# print the the first colum of RealEstate_USA Datasets "broked_by"
print(brokered_by)    
# print the the first colum of RealEstate_USA Datasets "Price"
print(price)
# print the the first colum of RealEstate_USA Datasets "Bed"
print(bed)
# print the the first colum of RealEstate_USA Datasets "Bath"
print(bath)
# print the the first colum of RealEstate Datasets_USA "House_size"
print(house_size)


# Static Operation Apply on "price" colum of (RealEstate_USA DataSet)

print("Mean of Price:" , np.mean(price))                       #Find (Mean) of "Price" colum RealEstate_USA Data
print("Meadin of Price:", np.median(price))                    #Find (Median) of "Price" colum RealEstate_USA Data
print("Average of Price:", np.average(price))                  #Find (Average) of "Price" colum RealEstate_USA Data
print("Average of Std:", np.std(price))                        #Find (Average) of "Price" colum RealEstate_USA Data
print("Percentile_25 of Price:", np.percentile(price,25))      #Find (Percentile_25) of "Price" colum RealEstate_USA Data
print("Percentile_50 of Price:", np.percentile(price,50))      #Find (Percentile_50) of "Price" colum RealEstate_USA Data
print("percentile_75 of Price:", np.percentile(price,75))      #Find (Percentile_75) of "Price" colum RealEstate_USA Data
print("Min of Price:", np.min(price))                          #Find (Min) of "Price" colum RealEstate_USA Data
print("Max of Price:", np.max(price))                          #Find (Max) of "Price" colum RealEstate_USA Data


#  Maths Operations Apply on "price" colum of (RealEstate_USA DataSet)

print("Square of price: ", np.square(price))      #Square of colum "price" RealEstate Data USA
print("Squareroot of price:", np.sqrt(price))     #Sqrt of colm "price" RealEstate Data USA
print("Power of price:", np.power(price,price))   #Power of colm "price" RealEstate Data USA
print("Abs of price:", np.abs(price))             #Abs of colm "price" RealEstate Data USA

# Arithmetic Operations Apply on "price", "bed" and "bath" colum of (RealEstate_USA DataSet)

addition = price + bed + bath
multiplication = price * bed * bath
sbstraction = price - bed - bath
division = price / bed / bath

print("Addition between three colum :" , addition)                  # Addition between three colum "price", "bed", "bath"
print("Multiplication between three colum :" , multiplication)      # Multiplication between three colum "price", "bed", "bath"
print("Sbstraction between three colum :" , sbstraction)            # Sbstraction between three colum "price", "bed", "bath"
print("Division between three colum :" , division)                  # Division between three colum "price", "bed", "bath"
# First of all price convert in pi_values

price_pi = (price/np.pi) + 1

# Trignomatic Function Apply on "price_pi" of (RealEstate_USA DataSet)

print("Sin of price:", np.sin(price_pi))                            # Sin of price_pi
print("Cos of price:", np.cos(price_pi))                            # Cos of price_pi
print("Tan of price:", np.tan(price_pi))                            # Tan of price_pi

# Trignomatic Function hyperbolic Apply on "price_pi" of (RealEstate_USA DataSet)

print("Sinh of price:", np.sinh(price_pi))                            # Sinh of price_pi
print("Cosh of price:", np.cosh(price_pi))                            # Cosh of price_pi
print("Tanh of price:", np.tanh(price_pi))                            # Tanh of price_pi

# Trignomatic Function inverse_hyperbolic Apply on "price_pi" of (RealEstate_USA DataSet)

print("arcSinh of price:", np.arcsinh(price_pi))                            # arcSinh of price_pi
print("arcCosh of price:", np.arccosh(price_pi))                            # arcCosh of price_pi
print("arcTanh of price:", np.arctanh(price_pi))                            # arcTanh of price_pi

# Find natural log and base log_10 of colum "bed", "price" and "bath" (RealEstate_USA DataSet)

print("Natural log of bed :", np.log(bed))                            # Calculate Natural log of colum "bed" 
print("Natural log of price :", np.log(price))                        # Calculate Natural log of colum "price" 
print("Natural log of bath :", np.log(bath))                          # Calculate Natural log of colum "bath" 

print("log10 of bed :", np.log10(bed))                            # Calculate log10 of colum "bed" 
print("log10 of price :", np.log10(price))                        # Calculate log10 of colum "price" 
print("log10 of bath :", np.log10(bath))                          # Calculate log10 of colum "bath" 


# Creat 2_Deminition Array between 2_colum "bed" and "bath"

D2_Array = np.array([bed,bath])
print("Dimention Array between Bed acd Bath:" , D2_Array)                # Print 2_Deminition Array between 2_colum "bed" and "bath"

print("Dimention of Array:", D2_Array.ndim)                              # Check the Dimention of Array........

print("Total number of Elements in this Array:" , D2_Array.size)         #Check the number of elements in this array.......
print("Size of Array:", D2_Array.size)                                   #Check the Size of Array.........

print("Data Type of Array:", D2_Array.dtype)                             # Check the data type of Array......

# Splicing of Array
print("All rows and first 5 colum:", D2_Array[:,0:5])                    #print All rows and first 5 colum.......

print("First row and 7 colum with 2 step:",D2_Array[:1,:7:2])            #print First row and 7 colum with 2 step.......


# indexing of Array
print("indexing of Array [0,1]:", D2_Array[0,2])                         #print indexing of Array [0,2]
print("indexing of Array [2,6]:", D2_Array[1,6])                         #print indexing of Array [2,6]

# Nditer use in loop 

for elem in np.nditer(D2_Array):
    print(elem)                                                          #print all elements one by one use nditer

# ndenumerate use in loop

for index, elem in np.ndenumerate(D2_Array):
    print(index, elem)                                                   #print all elements one by one use nditer with indexing of element

# Reshape the Array
print("Reshape the Arraya of D2_Array:", np.reshape(D2_Array,(1,-1)))               #print Reshape of D2_Array
print("Reshape the Arraya of D2_Array:", np.reshape(D2_Array,(1,-1)))               #print Reshape of D2_Array

ReShape_D2_Array= np.reshape(D2_Array,(1,-1))
print("Demention of Array:",np.ndim(ReShape_D2_Array))                              #check deminition of Array after Reshape  


