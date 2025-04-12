import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#10. Analyze how bike mileage changes as it gets older.
# Create bike age column (assuming 'Year' column exists)
df['Bike Age'] = 2025 - df['Registration Year']  # Assuming data is from 2025
# Plot Average Mileage by Bike Age
plt.figure(figsize=(10, 6))
sns.lineplot(x=df['Bike Age'], y=df['Mileage (km/l)'], marker='o', ci=None, color='blue')
plt.title("Average Mileage vs. Bike Age")
plt.xlabel("Bike Age (Years)")
plt.ylabel("Mileage (km per liter)")
plt.grid(True)
plt.show()