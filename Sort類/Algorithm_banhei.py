#初期値の設定

A = []
temp = True
while temp == True:
    p = int(input('リストの中身を設定して下さい。'))
    A.append(p)
    j = input('リストの中身はまだありますか？無ければNを入力して下さい。')
    if j == 'N':
        temp = False

#番兵の設定

d = int(input('見つけるデータを入力して下さい。'))
A.append(d)
i = -1
for n in A:
    i +=1
    if n == d:
        break

#結果の表示

if i == 5:
    print('そのようなデータはありませんでした。。')
else:
    print('{}番目にありました。'.format(i+1))