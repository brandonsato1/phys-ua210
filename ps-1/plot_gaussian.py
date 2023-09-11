import numpy as np
from matplotlib import pyplot as plt

curve = []
#empty aray
for x in range(10000):
    curve.append(np.random.normal(0.0,3.0,None))
    #for loop that makes 100 points on a random normal
fig, ax = plt.subplots(figsize =(10, 7))
#makes the figure
ax.hist(curve,bins = 100)
plt.show()
fig.savefig('gaussian.png')