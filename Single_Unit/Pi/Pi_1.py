import random
import matplotlib.pyplot as plt

T = 0
N = 1000

for i in range(N):
    x = random.random()
    y = random.random()

    if x**2 + y**2 < 1:
        T += 1
        plt.plot(x,y,'ro')
    else:
        plt.plot(x,y,'bo')

pi = 4*T/N
print(pi)
plt.grid(True)
plt.show()

