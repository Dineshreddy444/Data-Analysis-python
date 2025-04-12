import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#9. Resale Price Distribution per brand
plt.figure(figsize=(12, 8))
sns.boxplot(x='Brand', y='Resale Price (INR)', data=df)
plt.xticks(rotation=90)
plt.title('Resale Price Distribution per Brand')
plt.xlabel('Brand')
plt.ylabel('Resale Price (INR)')
plt.show()