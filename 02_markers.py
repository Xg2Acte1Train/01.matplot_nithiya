from matplotlib import pyplot as plt
import numpy as np

x = np.array([12,18,25,40,56])
y = np.array([78,123,389,400,576])

plt.plot(x, y, marker='o')
plt.show()

plt.plot(x, y, marker='D', ms=15) 
plt.show()

plt.plot(x, y, marker='*', ms=15, mec='r') 
plt.show()

plt.plot(x, y, marker='*', ms=15, mec='r', mfc='hotpink') 
plt.show()
