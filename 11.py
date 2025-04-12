import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")


#11. Identify which brand offers the best engine capacity for each fuel type.
# Group by Brand and Fuel Type, then calculate the average Engine Capacity
brand_fuel_engine = df.groupby(['Brand', 'Fuel Type'])['Engine Capacity (cc)'].mean().reset_index()

# Sort by highest engine capacity
brand_fuel_engine = brand_fuel_engine.sort_values(by='Engine Capacity (cc)', ascending=False)

# Plot Bar Chart
plt.figure(figsize=(12, 6))
sns.barplot(x='Brand', y='Engine Capacity (cc)', hue='Fuel Type', data=brand_fuel_engine, palette="viridis")

# Chart formatting
plt.title("Best Engine Capacity (cc) by Brand and Fuel Type")
plt.xlabel("Brand")
plt.ylabel("Average Engine Capacity (cc)")
plt.xticks(rotation=45)
plt.legend(title="Fuel Type")
#plt.grid(axis='y', linestyle="--", alpha=0.7)

# Show plot
plt.show()
