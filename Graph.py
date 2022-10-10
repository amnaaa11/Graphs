import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8]

y = [10,30,20,50,60,32,33,10,30]


plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,marker='*', markerfacecolor='red', markersize=9)

  
plt.xlabel('X axis')

plt.ylabel('Y axis')
  

plt.title('Graph title!')
  
plt.show()
