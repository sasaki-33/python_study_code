#オブジェクト指向インターフェース
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,1,100)
y = x**2

"""
#figureオブジェクトの生成
fig = plt.figure()
#figureオブジェクトの中にaxオブジェクトを生成
ax = fig.add_subplot(221)
#figureオブジェクトの中に複数のオブジェクトを生成できる
ax_1 = fig.add_subplot(222)
ax.plot(x,y)
ax_1.plot(x*2,y)
#実行
plt.show()
"""
#一つのaxオブジェクトに複数のグラフを描画する
fig = plt.figure(figsize = (12,8))
ax = fig.add_subplot(111)
x_1 = np.linspace(0,1,100)
y_1 = x_1
x_2 = np.linspace(0,1,100)
y_2 = x_2 **2
#ラベルを付加
ax.plot(x_1,y_1,label = 'y = x')
ax.plot(x_2,y_2,label = 'y = x^2')
ax.set_xlabel('x_value')
ax.set_xlabel('y_value')
plt.legend(loc = 'best')
plt.show()