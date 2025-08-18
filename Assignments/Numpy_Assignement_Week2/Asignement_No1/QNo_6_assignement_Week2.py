import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

# Creat 3D Array between "price", "house_size " and "arce_lot"

Dimention3Array = np.array([[price,house_size,acre_lot]])
print(Dimention3Array)
print("3D Array: ", Dimention3Array.ndim)