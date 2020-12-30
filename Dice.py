"""
#関数の定義
def random_in(i):
    import random
    count = 0
    W = False
    while W == False:
        count += 1
        a = random.randint(1,i)
        if a == i:
            W = True
    return count

#サイコロの最大数を出せる確率を表示
r = int(input('サイコロの面を入力。'))
count = random_in(r)
print('{}回目の試行で出現。'.format(count))
"""

import random
#サイコロの最大値が出る試行回数を数える関数の定義
def dice(i):
    T = False
    count = 0
    while T == False:
        me = random.randint(1,i)
        if me == i:
            T = True
            count += 1
        else :
            count += 1
    #回数の出力
    return count
i = int(input('サイコロの目を入力'))
print('{}面の最大値が出るのは{}回目でした。'.format(i,dice(i)))
