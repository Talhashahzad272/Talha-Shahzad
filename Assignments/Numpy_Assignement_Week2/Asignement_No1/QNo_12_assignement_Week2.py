import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

# Creat 2D Array between "price" and "house_size"

Dimention2Array = np.array([price,house_size])
print(Dimention2Array)
# Sin of price colum

print("Sin of price:", np.sin(Dimention2Array))

# Cos of price colum

print("Cos of price:", np.cos(Dimention2Array))
