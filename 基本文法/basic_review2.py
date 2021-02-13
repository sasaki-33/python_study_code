"""
#enumerateはインデックスと要素を取り出すことが出来る
A = [1,2,3]

for a,b in enumerate(A):
    #リストの要素番号と、要素を表示
    print('{0}:{1}'.format(a,b))

#ラムダ式
i = lambda a,b : a*b
print(i(3,4))
#ラムダ式で、リストの要素を二乗して新たなリストを作成する
list_1 = [1,2,3,4,5]
list_2 = list(map(lambda i : i**2,list_1))
print(list_2)

#ラムダ式でif文を使用
abc = (lambda x : 'True' if x%2==0 else 'False')
print(abc(4))
"""