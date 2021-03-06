

# 円周率を求める
## 概要
半径1の円に内接する正n角形と外接する正n角形から円周率πを求める。  
内接n角形の周は円の外周より小さく、外接n角形の周は円の外周より大きい性質を利用する。

## 例
n = 4の時  
内接する四角形の周は4√2、外接する四角形の周は8である。    
よってπは*2√2 < π　< 4*の数値となる。  
***
nを大きくするほど、内接正多角形の周の長さも外接正多角形の周の長さも、円周に近づくのでπが近似的に求まる。

## 式
 2 * sin(π/n) * n < 2π < 2 * tan(π/n) * n
= sin(π/n) * n < π < tan(π/n) * n

## コード

```py

import math

# 円周率を近似的に求める関数
def pi(n):
    in_polygons = 2*n*math.sin(math.radians(180/n))
    out_polygons = 2*n*math.tan(math.radians(180/n))

    return [in_polygons/2,out_polygons/2]

# n = 180のとき
i = pi(180)
print('{} < π < {}'.format(i[0],i[1]))
```

## 結果
n = 180として、正180角形についてπを求めた結果  
3.141433158711032 < π < 3.1419116870791655 となった。