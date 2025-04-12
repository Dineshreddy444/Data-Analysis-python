import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#6. Average depreciation rate over different brands.
df['Depreciation Rate (%)'] = ((df['Price (INR)'] - df['Resale Price (INR)']) / df['Price (INR)']) * 100
brand_depreciation = df.groupby('Brand')['Depreciation Rate (%)'].mean().reset_index()
brand_depreciation = brand_depreciation.sort_values(by='Depreciation Rate (%)')
plt.figure(figsize=(12, 6))
sns.lineplot(x='Brand', y='Depreciation Rate (%)', data=brand_depreciation, marker='o', color='blue')
plt.xlabel("Brand")
plt.ylabel("Average Depreciation Rate (%)")
plt.title("Average Depreciation Rate Over Different Brands (Seaborn)")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()