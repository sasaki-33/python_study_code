#関数を使用する

#関数の定義
def sort(r):
    wild,i = 0,1
    while i <= len(r)-1:
        j = i-1
        while j >=0:
            if r[j]>r[j+1]:
                wild = r[j]
                r[j] = r[j+1]
                r[j+1] = wild
                j -= 1
            else:
                break
        i += 1
    return r

#配列の挿入

a = []
i = int(input('配列の初期値を一つ入力'))
a.append(i)
bool_a = True
while bool_a == True:
    hantei = input('配列に挿入する数値が無ければ、Nを入力')
    if hantei == 'N':
        bool_a = False
    else:
        suuti = int(input('配列に挿入する数値を入力'))
        a.append(suuti)
        a = sort(a)

#結果の表示
print('挿入ソートで並び換えを行った結果は\n{}'.format(a))