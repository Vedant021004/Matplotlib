import matplotlib.pyplot as plt
import pandas as pd
batters = pd.read_csv('batter.csv')

plt.subplot(projection = '3d')
plt.scatter3D(batters['runs'],batters['avg'],batters['strike_rate'],marker='+')
plt.title('IPL batsman analysis')
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

batters = pd.read_csv('batter.csv')

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    batters['runs'],
    batters['avg'],
    batters['strike_rate'],
    marker='+'
)

ax.set_title('IPL Batsman Analysis')
ax.set_xlabel('Runs')
ax.set_ylabel('Average')
ax.set_zlabel('Strike Rate')

plt.show()



import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [6,4,7,8]
z = [9,6,7,4]
fig = plt.figure(figsize=(5,5))
ax = plt.subplot(projection = '3d')
ax.scatter3D(x,y,z, s =[100,100,100,100])
ax.plot3D(x,y,z,color = 'red')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

fig = plt.figure(figsize=(10,10))
ax = plt.subplot(projection='3d')


fig.colorbar(ax.plot_surface(X, Y, Z))
plt.show()




import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

delivery = pd.read_csv('IPL_Ball_by_Ball_2008_2022.csv')
temp_df = delivery[(delivery['ballnumber'].isin([1,2,3,4,5,6])) & (delivery['batsman_run']==6)]
grid = temp_df.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')
plt.figure(figsize=(10,10))
plt.imshow(grid)
plt.yticks(delivery['overs'].unique(), list(range(1,21)))
plt.xticks(np.arange(0,6), list(range(1,7)))
plt.colorbar()
plt.show()