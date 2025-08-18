import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

# Arithmetaic opreation apply on colum "price" and "house_size" of Real Estate Datasets

Addition = price + house_size
Substration = price - house_size
Multiplication = price * house_size

print("Addition between price and house_size:", Addition)
print("Substration between price and house_size:", Substration)
print("Multiplication between price and house_size:", Multiplication)