import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

Dimention2Array = np.array([price])
print(Dimention2Array)

# print size of price colum

print("size of price:", np.size(Dimention2Array))
# print shape of price colum

print("shape of price:", np.shape(Dimention2Array))

# print ndim of price colum

print("Ndim of price:", np.ndim(price))

# log of price colum

print("log of price:", np.log(Dimention2Array))

# log10 of price colum

print("log10 of price:", np.log10(Dimention2Array))

# Sin of price colum

print("Sin of price:", np.sin(Dimention2Array))

# Cos of price colum

print("Cos of price:", np.cos(Dimention2Array))

# tan of price colum

print("Tan of price:", np.tan(Dimention2Array))