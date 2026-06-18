import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('gayle-175.csv')
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%')
plt.show()
