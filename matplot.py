import matplotlib.pyplot as plt
# %matplotlib inline

x = [0, 2, 4, 6]
y = [1, 3, 4, 8]

plt.plot(x, y)

plt.xlabel('X values')
plt.ylabel('y values')
plt.title('Plot Example')
plt.legend(['Data'])

# Saving the plot
plt.savefig('plot1.png', dpi=350, bbox_inches='tight')
plt.show()