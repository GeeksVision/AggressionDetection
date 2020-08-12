import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

# %matplotlib inline

data_file_path = '/Users/ashnakhetan/Desktop/Ashna/ConnectedCars/IntersectionData.csv'
df = pd.read_csv(data_file_path, skiprows=1)
#df = df[['Sec', 'Car1', 'Car2', 'Car3']]
df = df.iloc[:, :4]
df

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = []
y = []
dz = []

cols = ['red', 'blue', 'yellow', 'green']
colours = []

# for r, row in enumerate(df):
#     #print(row)
#     print(row[1:])
#     for c, col in enumerate(row[1:], start=1):
#         x.append(row[0])
#         y.append(c)
#         dz.append(col)
#         #colours.append(cols[r])
zz = [100, 80, 60, 90, 90, 50, 80, 100, 45, 70, 100, 40, 60, 100, 30,
      50, 80, 25, 40, 60, 15, 30, 40, 10, 20, 20, 5, 10, 0, 0, 0, 0, 0]
# zz.append(df.iloc[:,1:4])
# print(zz)
# x_pos = df.iloc[:,:1]
# y_pos = [1,2,3]
# z_pos = np.zeros(numBars)

numBars = 33
x_pos = [10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6,
         5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]
y_pos = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1,
         2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
z_pos = np.zeros(numBars)

x_size = np.ones(numBars)
y_size = np.ones(numBars)
z_size = zz

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [10, 8, 6, 4, 2, 0]
# z = [100, 80, 60, 40, 20]

# dx = np.ones(10)
# dy = np.ones(10)
# dz = [10,20,30,40,50,60,70,80,90,100]

ax1.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='aqua')

plt.xlim(10, 0)
plt.ylim(1, 3)
ax1.set_zlim(0, 100)

ax1.set_xlabel('Time to Intersection')
ax1.set_ylabel('% of Vehicles in Level')
ax1.set_zlabel('Aggression Level')

plt.show()
