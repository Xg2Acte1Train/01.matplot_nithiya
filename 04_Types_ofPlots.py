from matplotlib import pyplot as plt
import numpy as np
# sudo pip install -U matplotlib to install matplotlib-3.3.4 
# apt-get remove -y python3-matplotlib to remove existing version. Then 3D will work
from mpl_toolkits import mplot3d

x = np.array([12,18,25,40,56])
y = np.array([78,123,389,400,576])

plt.scatter(x, y)
plt.show()

plt.scatter(x, y)
plt.scatter(y, x)
plt.show()

plt.scatter(x, y, color=np.array(["red","green","blue","yellow","black"]))
plt.show()

plt.scatter(x, y, c=np.array([10,30,50,70,90]), cmap='nipy_spectral')# viridis
plt.colorbar()
plt.show()

plt.scatter(x, y, s=np.array([100,200,500,1000,60]))
plt.show()

plt.scatter(x, y, s=np.array([100,200,500,1000,60]), alpha=0.5)
plt.show()

plt.axes(projection='3d').scatter3D(x,y) # plot3D
plt.show()

plt.bar(x,y)
plt.show()

plt.bar(x,y,color='red',width = 5)
plt.show()

plt.barh(x,y)
plt.show()

plt.hist(x)
plt.show()

plt.pie(x)
plt.show()

plt.pie(x, labels=["E","D","C","B","A"], startangle = 180)
plt.show()

plt.pie(x, labels=["E","D","C","B","A"], explode = [0.3, 0.1, 0, 0, 0], shadow = True)
plt.legend(title = "Employee Ratings")
plt.show() 

