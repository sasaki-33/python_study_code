"""
#リスト
A = [1,2,3]
#追加
A.append(4)
#削除
A.remove(1)
#変更
A[2] = 5
#要素の平均の算出
i = sum(A)/len(A)
#小数点以下の桁を3桁で表示
print('{:.3f}'.format(i))
#スライス1以上4未満表示
print(A[1:4])

#辞書型
B = {'a':1,'b':2,'c':3}
#追加
B['d'] = 4
#削除
del B['a']
#変更
B['b'] = 7
#要素の平均の算出
j = sum(B.values())/len(B)
#スライスは不可

#タプル
C = (1,2,3)
#追加、削除、変更不可
#平均の算出
k = sum(C)/len(C)
#スライス1以上4未満表示
print(C[1:4])

#セット
D = {1,2,3}
#追加
D.add(4)
#削除
D.remove(1)
#変更は困難
#平均の算出
l = sum(D)/len(D)
#順序を持たないのでスライスは不可
#集合演算
E = {1,2,3}
F = {3,4,5}
#和集合、差集合、積集合、排他的論理和
print(E|F)
print(E-F)
print(E&F)
print(E^F)

#リストからタプルへ、辞書からリストへ、辞書の値をセットに変換
G = ['a','b','c']
H = {'d':1,'e':2,'f':3}
print(tuple(G))
print(list(H))
print(set(H.values()))
#二つのリストから辞書型を作成
I = ['a','b','c']
J = [1,2,3]
print(type(dict(zip(I,J))))

#yield
def suuti(x):
    for xx in range(x):
        yield xx*2
for i in suuti(5):
    print(i)

#boolについて
K = [1,2,3,4,5]
#条件を満たすならTrueが、満たさないならばFalseが入る
L = [i%2==0 for i in K]
#同様
for i in range(10):
    print(i%2==0)
"""