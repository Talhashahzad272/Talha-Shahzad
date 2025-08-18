import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/ML_LinearRegression_Week4/zameencom-property-data-By-Kaggle-Short.csv",delimiter=";", index_col= "property_id",parse_dates=[14], date_format={'date_added': '%d-%m-%Y'})
print(df.to_string())
print(df.head())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.shape)

X= df["bedrooms"].values.reshape(-1,1)
y= df["price"].values.reshape(-1,1)

print(X)
print(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_tset = train_test_split(X,y,train_size=0.75,random_state=42)
print(X_train)
print(X_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
print(regressor.intercept_)
print(regressor.coef_)
def calc(slope,intercept,bedrooms):
    return slope*bedrooms + intercept

score = calc(regressor.coef_,regressor.intercept_,32)
print(score)
y_perd = regressor.predict(X_test)

df_pred = pd.DataFrame({"Actual": y_tset.squeeze() , "predicted": y_perd.squeeze()})

print(df_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_tset,y_perd)
mse = mean_squared_error(y_tset,y_perd)
rmse= np.sqrt(mse)
r2 = r2_score(y_tset,y_perd)

print(mae)
print(mse)
print(rmse)
print(r2)

