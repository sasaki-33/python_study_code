import matplotlib.pyplot as plt
import math
import numpy as np
x = np.linspace(0,1,100)
y = np.sqrt(1-x*x)
plt.plot(x,y)
plt.show() 