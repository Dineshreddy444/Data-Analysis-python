import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#5. Effect of City Tier on Resale Prices
#Box Plot: Compare resale price distribution across Tier 1, Tier 2, and Tier 3 cities.
plt.figure(figsize=(10, 6))
sns.boxplot(x=df["City Tier"], y=df["Resale Price (INR)"], palette='pastel')
plt.xlabel("City Tier")
plt.ylabel("Resale Price (INR)")
plt.title("Resale Price Distribution Across City Tiers (Seaborn)")
plt.grid(axis='y')
plt.show()