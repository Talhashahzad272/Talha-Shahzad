import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df)
from sklearn.datasets import make_blobs
X, y_true  = df.iloc[:,[0,1]]

plt.scatter(X[0], X[1], s=20);
plt.show()