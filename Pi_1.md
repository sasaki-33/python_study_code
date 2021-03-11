

# モンテカルロ法
## 概要
モンテカルロ法に基づきpythonで円周率を求める

## 手順
xy座標に(0,0)から一辺が1である正方形を用意する。  
正方形の内部には半径が1である単位円が含まれる。  
この正方形内にランダムにN個の点を配置する。  
ランダムに配置した点が単位円の内部*(x^2+y^2<1)*にあれば、Tに1を加算する。    
正方形における単位円内に存在するTの割合はT/Nで求められる。  
***
単位円の面積をS1、正方形の面積をS2とする。    
正方形内の単位円の割合は、*S1/S2*である。  
正方形内に配置する点が多いほど面積に近づくので、πの数値が求められる。  

## 式
S1 = 1×1×π×1/4 = π/4  
S2 = 1×1 = 1  
S1/S2 = π/4  
π/4 = T/N  

π = 4T/N

## コード

```py 

import random
import matplotlib.pyplot as plt

# 初期値の設定
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
# 結果の表示
print(pi)
plt.grid(True)
# プロットの表示
plt.show()
```
