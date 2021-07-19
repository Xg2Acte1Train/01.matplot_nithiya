from matplotlib import pyplot as plt
import numpy as np

x = np.array([12,18,25,40,56])
y = np.array([78,123,389,400,576])

plt.plot(x, y, linestyle = 'dotted') 
plt.show()

plt.plot(x, y, ls = '--') 
plt.show()

plt.plot(x, y, ls = '--', color='#4CAF55') 
plt.show()

plt.plot(x, y, c='r', lw='20.5') 
plt.show()

plt.plot(x, y, '+:r')
plt.show()





