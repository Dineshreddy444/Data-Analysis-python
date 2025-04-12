import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")

#7. Average price & resale price over years
plt.figure(figsize=(10, 6))
df.groupby('Year of Manufacture')[['Price (INR)', 'Resale Price (INR)']].mean().plot(kind='line')
plt.title('Average Price and Resale Price Over Years')
plt.ylabel('Price (INR)')
plt.xlabel('Year of Manufacture')
plt.legend(["Avg Price", "Avg Resale Price"])
plt.grid(True)
plt.show()