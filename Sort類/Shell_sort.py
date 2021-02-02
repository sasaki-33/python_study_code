#数字を入力し並び替えを行う配列を作成
A = []
T = False
while T == False:
    i = int(input('数字を一つ入力'))
    A.append(i)
    End = input('数字入力を終了するならNを入力')
    if End == 'N':
        T = True

#数字を比較する間隔を決める
h = int(len(A)/2)

#並び替えを行う関数の定義
def hikaku(A,x,y):
    w = 0
    if A[x] > A[x+y]:
            w = A[x]
            A[x] = A[x+y]
            A[x+y] = w
    return A
#並び替え前のリストの表示
print(A)

#間隔hが0になれば終了
while h > 0:
    j = 0
    #並び替え対象の二つ目の要素番号は、リストの最後の要素番号まで繰り返す
    while j + h <= len(A) -1:
        #A[j+h]がA[j]より小さいならば関数呼出し
        if A[j] > A[j+h]:
           hikaku(A,j,h)
           #さらに前方に要素が存在するなら関数呼び出し
           if j-h >= 0:
               hikaku(A,j-h,h)
        j += 1
    #最後の間隔hが1となるようにhの偶奇で調整
    if h%2 == 1:
        h -= 2
    else:
        h -= 1

#並び替えたリストを表示
print(A)