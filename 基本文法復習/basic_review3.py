"""
#zip関数
A = [1,2,3]
B = [4,5,6]
for a,b in zip(A,B):
    print(a,b)

#zip関数を用いて二つのリストから辞書型を作成
C = ['a','b','c']
D = [7,8,9]
E = dict(zip(C,D))

#リスト内包表記
F = [1,2,3]
#Fの要素をそれぞれ二乗してリストを作成
G = [x**2 for x in F]

#リスト内包表記でif文の利用
H = [1,2,3,4]
#要素が偶数ならば4倍を行う
I = [x*4 for x in H if x%2 ==0]
#条件分岐の場合
J = [1,2,3,4]
K = [x*3 if x%2==0 else x*2 for x in J]

#zip,enumerateを使用したリスト内包表記
L = [1,2,3]
M = ['a','b','c']
N = [(x[0],x[1]) for x in zip(L,M)]
O = [(x[0],x[1]) for x in enumerate(M)]

#セット(集合)内包表記
P = [1,2,3]
Q = {x**2 for x in P}
print(Q)
"""