import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Full_Stack_Ai_inpython/Assignments/Pandas_Assignement_Week2/Assignement_No1/RealEstate-USA.csv", delimiter=",")

# print all data of Real Estate in datafaram

print(df)

# Draw - Line Plot, with X parameter – as “city“ and y parameter as “price”
# https://seaborn.pydata.org/generated/seaborn.lineplot.html
# Study and Analyze the output graph.

sns.set_theme(style="darkgrid")
sns.lineplot(x="city", y= "price", data=df )

plt.show()

