import pandas as pd
import matplotlib.pyplot as plt

plt.style.available
plt.style.use('tableau-colorblind10')

# df = pd.read_csv("sharma-kohli.csv")
# plt.plot(df['index'], df['V Kohli'],color = "green",marker = 'o', label = 'virat')
# plt.plot(df['index'], df['RG Sharma'],color = "black",marker = 'o',label = 'Rohit')
# plt.grid()
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

df = pd.read_csv('batsman_season_record.csv')
print(df)
plt.plot(df['batsman'],df['2017'],label='2017')
plt.scatter(df['batsman'],df['2017'],label='2017')
plt.bar(df['batsman'],df['2017'],label='2017')
plt.grid()
# plt.savefig("graph.png")
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('gayle-175.csv')
myexplode = [0.1, 0.1, 0.1, 0.1,0.1,0.1]
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%', explode = myexplode, shadow = True)
plt.savefig("sample.png")
plt.show()







import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('batsman_season_record.csv')

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(df['batsman'], df['2017'])
plt.title("Line Plot")

plt.subplot(1,3,2)
plt.bar(df['batsman'], df['2017'])
plt.title("Bar Plot")

plt.subplot(1,3,3)
plt.scatter(df['batsman'], df['2017'])
plt.title("Scatter Plot")

plt.tight_layout()
plt.show()





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


