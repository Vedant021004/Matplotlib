import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("sharma-kohli.csv")
# plt.plot(df['index'], df['V Kohli'],color = "green",marker = 'o', label = 'virat')
# plt.plot(df['index'], df['RG Sharma'],color = "black",marker = 'o',label = 'Rohit')
# plt.grid()
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('batsman_season_record.csv')
print(df)
plt.plot(df['batsman'],df['2017'],label='2017')
plt.scatter(df['batsman'],df['2017'],label='2017')
plt.bar(df['batsman'],df['2017'],label='2017')
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%')
plt.grid()
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('gayle-175.csv')
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%')
plt.show()
