"""
クイックソート
軸となる基準値を変数pivotに設定し、pivot未満からなる配列の範囲とpivot以上からなる配列の範囲を作成し、
この作業を再帰的に行うことで、数値を昇順に整列するアルゴリズムである。
以下のプログラムでは、配列内をpivot未満とpivot以上の数値に分ける関数arrangeと、基準値を設定するfind_pivotと、
範囲を設定し、再帰処理を行い配列を返すquick_sortを使う。
"""

#配列の範囲内の最小要素番号と最大要素番号を引数とする
def arrange(A,min,max,pivot):
    l = min
    r = max
    #pivot未満の要素がmin～l-1、pivot以上の要素がl～maxにくるようにする
    while l <= r:
        tmp = A[l]
        A[l] = A[r]
        A[r] = tmp
        while A[l] < pivot:
            l += 1
        while A[r] >= pivot:
            r -= 1
    #pivotの要素番号をretとする
    ret = l
    #retを返す
    return ret

#引数として渡した配列とその範囲内からpivotを見つけ出す
def find_pivot(A,min,max):
    #配列の最初の要素を基準値とする
    pivot = A[min]
    k = min + 1
    ret = -1
    found = False
    #A[min]と異なる要素を見つけ、値が大きいほうを基準値とする
    while k <= max and found == False:
        if A[k] == pivot:
            k += 1
        else :
            found = True
            if A[k] > pivot:
                ret = k
            else:
                ret = min
    #基準値とする要素の要素番号retを返す
    return ret


def quick_sort(A,min,max):
    j = find_pivot(A,min,max)
    if j > -1:
        pivot = A[j]
        k = arrange(A,min,max,pivot)
        l = k-1
        #基準値未満の値を集めた配列について再帰処理
        quick_sort(A,min,l)
        #基準値以上の値を集めた配列について再帰処理
        quick_sort(A,k,max)
    #整列済みの配列Aを返す
    return A

#適当な配列を用意
A = [3,5,4,7,1,2,8,9,6,0]
#整列済みの配列をBに設定
B = quick_sort(A,0,len(A)-1)
#結果の表示
print(B)