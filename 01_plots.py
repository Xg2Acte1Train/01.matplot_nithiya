from matplotlib import pyplot as plt
import numpy as np

y = np.array([78,123,389,400,576])
plt.plot(y)
plt.show()

x = np.array([12,18,25,40,56])
plt.grid()
plt.plot(x, y)
plt.show()

fig = plt.figure(figsize=(2,2))
plt.plot(x, y)
plt.show()

plt.plot(x, y)
plt.xlim(10,100)
plt.ylim(100,1000)
plt.show()

plt.plot(x, y, 'o')
plt.title("NM Company",loc = 'right')
plt.xlabel("incentive percentage", fontdict = {'family':'serif','color':'blue','size':20})
plt.ylabel("sales")
plt.xticks(rotation=45)
plt.show()

plt.grid(axis = 'y',color = 'green', linestyle = '--', linewidth = 0.5)
plt.plot(x) # plt.clf()
plt.plot(y)
plt.show()
plt.savefig("./chart.png")

plt.subplot(2, 3, 1)
plt.plot(x)

plt.subplot(2, 3, 2)
plt.plot()

plt.subplot(2, 3, 3)
plt.plot(y)

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title('Incentive vs sales')

plt.suptitle("Company details")
plt.show()

