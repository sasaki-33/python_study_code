#配列の用意
A = []

#入力で配列の作成
bool_a = True
while bool_a == True:
    atai = int(input('配列の値を入力'))
    A.append(atai)
    hantei = input('他の要素が無ければNを入力')
    if hantei == 'N':
        bool_a = False

#配列の表示
print('用意した配列は\n{}'.format(A))
print('バブルソートで昇順に並び替えを行う。')

#バブルソートで配列の値を並び替え
i = len(A)-1
wild = 0
while i >=1:
    j = 0
    while j <= i-1:
        if A[j] > A[j+1]:
            wild = A[j]
            A[j] = A[j+1]
            A[j+1] = wild
        j += 1
    i -= 1

#結果の表示
print('並び替えた配列は\n{}'.format(A))