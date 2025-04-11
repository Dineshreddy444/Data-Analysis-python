import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#3. Most Popular Bike Brands
top_brands = df['Brand'].value_counts().nlargest(10)
plt.figure(figsize=(10, 7))
plt.bar(top_brands.index, top_brands.values, color='skyblue', edgecolor='black')
plt.xlabel("Bike Brand")
plt.ylabel("Number of Bikes Sold")
plt.title("Top-Selling Bike Brands")
plt.xticks(rotation=45)
plt.show()