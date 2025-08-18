import numpy as np

brokered_by, price, acre_lot, city, house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)
 
# Stats opreation apply on price colum of Real Estate data 

print("Real Estate Mean of price:",np.mean(price))
print("Real Estate Median of price:",np.median(price))
print("Real Estate Average of price:",np.average(price))
print("Real Estate STD of price:",np.std(price))
print("Real Estate Percentile_25 of price:",np.percentile(price,25))
print("Real Estate percential_50 of price:",np.percentile(price,50))
print("Real Estate persential_75 of price:",np.percentile(price,75))
print("Real Estate Min of price:",np.min(price))
print("Real Estate Max of price:",np.max(price))
 