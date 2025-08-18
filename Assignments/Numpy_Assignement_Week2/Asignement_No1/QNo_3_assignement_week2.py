import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

# State operation apply on house size of Real Estate Data


print("Real Estate Mean of house_size:",np.mean(house_size))
print("Real Estate Median of house_size:",np.median(house_size))
print("Real Estate Average of house_size:",np.average(house_size))
print("Real Estate STD of house_size:",np.std(house_size))
print("Real Estate Percentile_25 of house_size:",np.percentile(house_size,25))
print("Real Estate percential_50 of house_size:",np.percentile(house_size,50))
print("Real Estate persential_75 of house_size:",np.percentile(house_size,75))
print("Real Estate Min of house_size:",np.min(house_size))
print("Real Estate Max of house_size:",np.max(house_size))
