import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#4. Impact of Engine Capacity on Resale Value
#Scatter Plot: Compare engine capacity vs. resale price.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Engine Capacity (cc)', y='Resale Price (INR)', data=df, color='blue', alpha=0.5)
plt.xlabel("Engine Capacity (cc)")
plt.ylabel("Resale Price (INR)")
plt.title("Impact of Engine Capacity on Resale Value (Seaborn)")
plt.grid(True)
plt.show()