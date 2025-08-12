import numpy as np

# load data in csv file of Startup_Growth
Startup_Name, Industry, Investment_Amount_USD, Valuation_USD,Number_of_Investors = np.genfromtxt("Full_Stack_DataScience_inpython\Startup_Growth_Dataset\startup_growth_investment_data.csv", delimiter=",", usecols=(0,1,3,4,5),unpack=True,dtype= None, skip_header=1)
np.set_printoptions(threshold=np.inf)

# print all colums data with name
print(Startup_Name)
print(Industry)
print(Investment_Amount_USD)
print(Valuation_USD)
print(Number_of_Investors)


#Startup Dataset (Investment_Amount_USD)  - statistics operations
print("Startup Growth Dataset (Investment_Amount_USD) mean:", np.mean(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) median:", np.median(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) Std:", np.std(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) Average:", np.average(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) percentile_25:", np.percentile(Investment_Amount_USD,25))
print("Startup Growth Dataset (Investment_Amount_USD) percentile_50:", np.percentile(Investment_Amount_USD,50))
print("Startup Growth Dataset (Investment_Amount_USD) percentile_75:", np.percentile(Investment_Amount_USD,75))
print("Startup Growth Dataset (Investment_Amount_USD) min:", np.min(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) max:", np.max(Investment_Amount_USD))


#Startup Dataset (Investment_Amount_USD) - maths operations

print("Startup Growth Dataset (Investment_Amount_USD) square", np.square(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) sqrt", np.sqrt(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) power", np.power(Investment_Amount_USD,Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) abs", np.abs(Investment_Amount_USD))

# Perform basic arithmetic operations
print("Startup Growth Dataset (InvestDment_Amount_US)-(Valuation_USD) , addition", Investment_Amount_USD + Valuation_USD )
print("Startup Growth Dataset (InvestDment_Amount_US)-(Valuation_USD) , substraction", Investment_Amount_USD - Valuation_USD )
print("Startup Growth Dataset (InvestDment_Amount_US)-(Valuation_USD) , Multiplaction", Investment_Amount_USD * Valuation_USD )
print("Startup Growth Dataset (InvestDment_Amount_US)-(Valuation_USD) , Division", Investment_Amount_USD / Valuation_USD )


#Trigonometric Functions
print("Startup Growth Dataset (Investment_Amount_USD) sin", np.sin(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) cos", np.cos(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) tan", np.tan(Investment_Amount_USD))

# Calculate the natural logarithm and base-10 logarithm
print("Startup Growth Dataset (Investment_Amount_USD) log", np.log(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) log10", np.log10(Investment_Amount_USD))


#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
print("Startup Growth Dataset (Investment_Amount_USD) sinh", np.sinh(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) cosh", np.cosh(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) tanh", np.tanh(Investment_Amount_USD))

# Calculate the inverse hyperbolic sine of each element
print("Startup Growth Dataset (Investment_Amount_USD) asinh", np.asinh(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) acosh", np.acosh(Investment_Amount_USD))
print("Startup Growth Dataset (Investment_Amount_USD) atanh", np.atanh(Investment_Amount_USD))


# Startup Growth Dataset (Investment_Amount_USD) (Valuation_USD) - 2 dimentional arrary


D2array = np.array([Number_of_Investors,Investment_Amount_USD])
# print(D2array)
print(D2array)
#  check the dimension of array1
print("Startup Growth Dataset Dimention of Array:" , D2array.ndim)
#  check the size of array1
print("Startup Growth Dataset Dimention of Array:" , D2array.size)
#  check the shape of array1
print("Startup Growth Dataset Dimention of Array:" , D2array.shape)
#  check the dtype of array1
print("Startup Growth Dataset Dimention of Array:" , D2array.dtype)


#  Startup Growth Dataset Splicing of array
print("Splicing of Array between rows and colum:", D2array[1:5,2:6])

#  Startup Growth Dataset Splicing of array with step
print("Splicing of Array between rows and colum:", D2array[1:5,2:6,2])

# Startup Growth Dataset Indexing array
print("indexing of row and colum with step:", D2array[1,2,3])
print("indexing of multiple rows:", D2array[[12,45,3]])
print("indexing of single row and multiple colum:", D2array[12,[1,2,5]])


#You should use the builtin function nditer, if you don't need to have the indexes values

for elem in np.nditer(D2array):
    print(elem)


#EDIT: If you need indexes (as a tuple for 2D table), then:

for index,elem in np.ndenumerate(D2array):
    print(index,elem)


# 1 x 4000 ========>>>>> 1  x 4000 - reshape
reshape_D2arra = np.reshape(D2array,(1,4000))

print(reshape_D2arra)
print(reshape_D2arra.ndim)
print(reshape_D2arra.shape)
print(reshape_D2arra.dtype)











