import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_RealEstate = pd.read_csv("Full_Stack_Ai_inpython//Assignments//ML_LinearRegression_Week4//Real_Estate_Sales_2001-2022_GL-Short.csv", delimiter="," , index_col="Serial Number",parse_dates=[2], date_format={'date_added': '%d-%m-%Y'})

# df = pd.read_csv('test.csv', na_filter= False)
print(df_RealEstate)


print(df_RealEstate.info())

print(df_RealEstate.dtypes)

print(df_RealEstate.describe())

print(df_RealEstate.shape)

df_RealEstate.plot.scatter(x = "Assessed Value", y = "Sale Amount")
plt.show()

X= df_RealEstate["Assessed Value"].values.reshape(-1,1)
y= df_RealEstate["Sale Amount"].values.reshape(-1,1)

print("Values of x:",X)
print("Values of y:",y)

SEED = 2

from sklearn.model_selection import train_test_split

X_train , X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=2)

print(X_train)
print(X_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train,y_train)

print(regressor.intercept_)

print(regressor.coef_)

def calc(slope,intercept,Assessed_Value):
    return slope*Assessed_Value + intercept

score = calc(regressor.coef_, regressor.intercept_, 150500.00 )
print(score)
print("Score print:")
score = regressor.predict([[150500.00]])
print(score)
y_perd = regressor.predict(X_test)

df_pred = pd.DataFrame({"Actual": y_test.squeeze() , "predicted": y_perd.squeeze()})

print(df_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test,y_perd)
mse = mean_squared_error(y_test,y_perd)
rmse= np.sqrt(mse)
r2 = r2_score(y_test,y_perd)

print(mae)
print(mse)
print(rmse)
print(r2)






