import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.plot(x, z)
ax.set_title("Functions")
ax.legend(['Sin', 'Cos'])
ax.xaxis.set_label_text('Angle')
ax.yaxis.set_label_text('Sine and Cosine')


# Saving the plot
plt.savefig('plot2.png', dpi=350, bbox_inches='tight')
plt.show()