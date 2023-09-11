import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
grouped = df.groupby('country')['finalWorth'].mean().reset_index()
plt.bar(grouped['country'], grouped['finalWorth'])
plt.xlabel('country')
plt.ylabel('')
plt.title('Bar Plot by Category')
plt.show()
