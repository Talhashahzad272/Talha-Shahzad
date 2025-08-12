import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_RealEstate = pd.read_csv("Full_Stack_DataScience_inpython\RealEstate_Dataset\RealEstate-USA.csv",delimiter=",")
print("Data of RealEstate:", df_RealEstate)

# Take first 50 rows of RealEstate Datasets

dffilter = df_RealEstate.head(50)
print(dffilter)


#kind='hist'
# Graph 1
g = sns.displot(data= dffilter, x = "price", y = "bed")
g.figure.suptitle("Displot graph between price and bed")
plt.show()

#kind='kde'
# Graph 2
g = sns.displot(data= dffilter, x = "price", y = "bath")
g.figure.suptitle("Displot Graph between price and bath:")
plt.show()

# Graph 3
g = sns.kdeplot(data=dffilter, x = "price", y="bath")
g.figure.suptitle("Kdeplot Graph between price and bath:")
plt.show()

# Graph 4
g = sns.histplot(data=dffilter, x = "price", y="bath")
g.figure.suptitle("Histplot Graph between price and bath:")
plt.show()

# Graph 5
g = sns.scatterplot(data=dffilter, x = "price", y="bath")
g.figure.suptitle("Scatterplot Graph between price and bath:")
plt.show()

# Graph 6
g = sns.barplot(data=dffilter, x = "price", y="bath")
g.figure.suptitle("Barplot Graph between price and bath:")
plt.show()

# Graph 7
g = sns.catplot(data=dffilter, x = "bath", y="price")
g.figure.suptitle("Catplot Graph between price and bath:")
plt.show()

# Graph 8
corr = dffilter[["price","bath"]].corr()
g = sns.heatmap(corr,annot=True,cmap="coolwarm")
g.figure.suptitle("Heatmap Graph between price and bath:")
plt.show()