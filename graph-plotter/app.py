import matplotlib.pyplot as plt

x1 = [2,5,6,7,8]
y1 = [2,3,6,1,2]

plt.plot(x1,y1,color="green", linestyle="dashed", linewidth="3",marker="o", markerfacecolor="blue", markersize="12", label = 'Line 1')

plt.ylim(0,8)
plt.xlim(0,10)

#x2 = [1,3,6,7]
#y2 = [4,6,7,7]

#plt.plot(x2,y2,label = 'Line 2')


plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Graph")
plt.legend()
plt.show()