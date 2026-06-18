# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# year = np.array([2000,2001,2002,2003,2004,2005,2006])
# sales = np.array([10,15,20,25,30,35,40])

# plt.plot(year, sales,color="green")
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.title("Sales Trend")
# plt.show()





# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [10,20,30,40,50]

# plt.plot(x,y,color="red",marker="o")
# plt.grid()
# plt.show()


# import matplotlib.pyplot as plt

# students = ["A","B","C","D"]
# marks = [80,60,90,70]

# plt.bar(students,marks,color="black")
# plt.scatter(students,marks)

# plt.grid()
# plt.show()


# import matplotlib.pyplot as plt

# height = [150,160,170,180]
# weight = [45,55,65,75]

# plt.scatter(height,weight)

# plt.show()



import matplotlib.pyplot as plt

children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']
myexplode = [0.1, 0.1, 0.1, 0.1,0.1]

plt.bar(colors,children,color='black')

plt.show()


plt.pie(children, labels = colors, startangle = 90)
plt.show()
plt.pie(children, labels = colors, explode = myexplode, shadow = True)
plt.legend(title = 'Color Data')
plt.show()






