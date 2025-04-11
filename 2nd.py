import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")
#2. Histogram for Mileage Distribution
#Distribution of mileage across different bikes
plt.figure(figsize=(10, 6))
sns.histplot(df['Mileage (km/l)'], bins=30, kde=True, color='green')
plt.title('Distribution of Mileage')
plt.xlabel('Mileage (km/l)')
plt.ylabel('Frequency')
plt.show()