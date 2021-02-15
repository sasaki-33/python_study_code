#オブジェクト指向インターフェース
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,1,100)
y = x**2

#figureオブジェクトの生成
fig = plt.figure()
#figureオブジェクトの中にaxオブジェクトを生成
ax = fig.add_subplot(111)
#figureオブジェクトの中に複数のオブジェクトを生成できる
ax_1 = fig.add_subplot(211)
ax.plot(x,y)
ax_1.plot(x*2,y)
plt.show()