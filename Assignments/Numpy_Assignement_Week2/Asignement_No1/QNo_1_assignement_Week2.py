import numpy as np

brokered_by,price,acre_lot,city,house_size = np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,5,7,10),unpack=True,dtype=None,skip_header=1)

print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

# static opreation apply on RealEstate USA data base

print("Real Estate Mean:",np.mean(price))
print("Real Estate Median:",np.median(price))
print("Real Estate Average:",np.average(price))
print("Real Estate STD:",np.std(price))
print("Real Estate Percentile_25:",np.percentile(price,25))
print("Real Estate percential_50:",np.percentile(price,50))
print("Real Estate persential_75:",np.percentile(price,75))
print("Real Estate Min:",np.min(price))
print("Real Estate Max:",np.max(price))
