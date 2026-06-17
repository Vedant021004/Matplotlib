import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sharma-kohli.csv")
plt.plot(df['index'], df['V Kohli'],color = "green",marker = 'o', label = 'virat')
plt.plot(df['index'], df['RG Sharma'],color = "black",marker = 'o',label = 'Rohit')
plt.grid()
plt.show()
plt.legend()
