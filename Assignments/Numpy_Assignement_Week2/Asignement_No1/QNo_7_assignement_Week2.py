import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)


Dimention1Array = np.array(price)
print(Dimention1Array)

# Use Nditer through for loop on colum price

for num in np.nditer(Dimention1Array):
    print(num)