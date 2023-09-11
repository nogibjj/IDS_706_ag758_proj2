import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("World University Rankings 2023.csv")

grouped = df.groupby('country')['finalWorth'].mean().reset_index()
plt.bar(grouped['country'], grouped['finalWorth'])
plt.xlabel('country')
plt.ylabel('')
plt.title('Bar Plot by Category')
plt.show()
