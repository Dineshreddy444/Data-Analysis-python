import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#8. Heatmap: Correlation between numerical features
corr = df[['Price (INR)', 'Engine Capacity (cc)', 'Mileage (km/l)', 'Resale Price (INR)', 'Avg Daily Distance (km)']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numerical Features')
plt.show()