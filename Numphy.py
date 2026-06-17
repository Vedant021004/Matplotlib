import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



x = np.random.randint(1,100,20)
y = np.random.randint(1,100,20)

plt.plot(x,y,color = "black")
plt.grid()
plt.show()