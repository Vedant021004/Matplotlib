import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('batter.csv')
sample_df = df.head(100).sample(25,random_state=5)
plt.scatter(sample_df['runs'],sample_df['avg'])
plt.figure(figsize=(18,10))
plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs'])

for i in range(sample_df.shape[0]):
  plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i])
plt.colorbar()
plt.show()