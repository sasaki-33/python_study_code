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