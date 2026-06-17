import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

year = np.array([2000,2001,2002,2003,2004,2005,2006])
sales = np.array([10,15,20,25,30,35,40])

plt.plot(year, sales)
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.show()

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x,y,color="red")
plt.show()