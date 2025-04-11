import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"c:\Users\Dinesh_reddy\Downloads\python ca 2.csv")
#1. Sales Contribution by Seller Type
seller_counts = df['Seller Type'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(seller_counts, labels=seller_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral'], startangle=140)
plt.title("Sales Contribution by Seller Type (Pie Chart)")
plt.show()
