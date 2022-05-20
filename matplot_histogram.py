import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('fivethirtyeight')

mu = 80
sigma = 7
x = np.random.normal(mu, sigma, size=200)

fig, ax = plt.subplots()

ax.hist(x, 20)
ax.set_title("Histogram")
ax.xaxis.set_label_text('Bin Range')
ax.yaxis.set_label_text('Frequency')


# Saving the plot
plt.savefig('histogram.png', dpi=350, bbox_inches='tight')
plt.show()