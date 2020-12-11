#切り捨てを行うためのmathの宣言
import math

#数値を比較し並べ直し、結合するmerge関数の定義
def merge(slist1,num1,slist2,num2,list):
    i,j = 0,0
    #どちらかのリストの内容が無くなるまで繰り返す
    while i<num1 and j<num2:

        #数値が小さい方を先に格納
        if slist1[i]<slist2[j]:
            list[i+j] = slist1[i]
            i += 1
        #片方の数値を格納
        else:
            list[i+j] = slist2[j]
            j += 1
    #数値が余っているリストが存在する時、listの一番後ろにその数値を格納
    while i<num1 or j<num2:
        #slistの数値が余っている時
        if i<num1:
            list[i+j] = slist1[i]
            i += 1
        #slist2の数値が余っている時
        else:
            list[i+j] = slist2[j]
            j += 1
    
    #呼び出したsort関数にlistを返却
    return list

#二つのlistに分解しmerge関数を呼び出す再帰的なsort関数の定義
def sort(list,num):

    #listの中の数値が2個以上の時実行
    if num>1:
        #個数の分配
        num1 = math.floor(num/2)
        num2 = num - num1
        slist1 = []
        slist2 = []
        i = 0
        #分割し新たなnum1個のリストの作成
        while i<num1:
            slist1.append(list[i])
            i += 1
        j = 0
        #分割し新たなnum2個のリストの作成
        while j<num2:
            slist2.append(list[j+num1])
            j += 1
        #再帰的にsortを呼出し、listの中の数値が1個になれば次のコードを実行
        sort(slist1,num1)
        #再帰的にsortを呼出し、listの中の数値が1個になれば次のコードを実行
        sort(slist2,num2)
        #再帰的にmergeを呼出し
        merge(slist1,num1,slist2,num2,list)

        #mergeから出力されたlistをさらに出力
        return list

#sort関数の呼出し
list = [5,7,3,1,6,8,2,4,9]
num = 9
#結果の表示
print(sort(list,num))