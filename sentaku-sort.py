#リスト作成 or 他データ読み込み
A = []

#入力で配列の作成
bool1 = True
while bool1 == True:
    X = int(input('配列の値を入力'))
    A.append(X)
    bool2 = input('他の要素が無ければNを入力')
    if bool2 == 'N':
        bool1 = False

#配列の表示
print('整列前の配列は\n{}'.format(A))
print('選択ソートで昇順に並び替えをする。')

#選択ソートを行う
a,b,c = 0,0,0
while a <= len(A)-2:
    b = a
    j = a + 1
    while j <= len(A)-1:
        if A[b] > A[j]:
            b = j
        j += 1
    
    if a != b:
        w = A[a]
        A[a] = A[b]
        A[b] = w
    a += 1

#結果の表示
print('並び替えた配列は\n{}'.format(A))