# Django学習記録(day10)
## レコードの並び替え
今までレコードは、ID番号が昇順に並べられていた  
他の基準でレコードを並び替える方法として、Managerの「order_by」というメソッドを使用する方法がある  
* Human(モデル名).objects.all.(filter).order_by(項目名) ・・・項目を昇順に並び替える  
* Human.objects.all(filter).order_by(項目名).reverse ・・・項目を降順に並び替える（reverseメソッドを使用する）

## レコードの指定
テーブルから取り出されるレコードは、QuerySetというクラスのインスタンスであり、リストと同様に添え字を使用し、取り出すレコードを指定できる  
* Human.objects.all()[0:4] ・・・添え字番号が0から4未満のレコード(1<=id<=4)
[]の中は整数型なので、フォームで文字型の数字を記入した場合、int型に直して指定する  

## レコードの集計
allやfilterで値を取り出し、合計や平均を算出することも可能だが、django.db.modelsには「aggregate」というメソッドが存在する  
* Human.objects.aggregate(関数) ・・・関数には以下の機能がある  
1. Count(項目名) ・・・指定した項目のレコード数を返す
2. Sum(項目名) ・・・指定した項目の合計値を返す
3. Avg(項目名) ・・・指定した項目の平均を返す
4. Min(項目名) ・・・指定した項目の最小値を返す
5. Count(項目名) ・・・指定した項目の最大値を返す  

## SQLの実行方法
SQLデータベースは、SQLのクエリでデータベースと情報のやり取りを行うため、Djangoの中から直接SQLクエリを実行できる  
モデルのobjectsに設定されているオブジェクトに「Manager」クラスが用意されている  
「Manager」クラスは、データベースクエリを操作するための機能を提供するもので、メソッドなどの内部から、SQLクエリを作成しデータベースに渡している  
このManagerクラスに「raw」というメソッドが用意されており、これを使用し直接SQLクエリをデータベースに渡す  
find関数を編集し、  
```python
def find(request):
    # POST送信された場合の処理
    if(request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        # SQLの構文(全て選択)
        sql = 'select * from test_human'
        if (msg != ''):
            # whereで条件を付ける
            sql += ' where ' + msg
        # rawで直接SQLを実行させる
        data = Human.objects.raw(sql)
        msg = sql
    else:
        msg = 'search data'
        form = FindForm()
        data = Human.objects.all()
    params = {
        'title':'your data',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'test/find.html', params)
```  
* 「select * from テーブル名」で、テーブルから全てを選択する  
テーブル名は、「アプリケーション名_モデル名」という形で指定する  

### SQL構文
1. あいまい検索  
「項目名 like 値」・・・値は「%値%」で値が含まれるもの、「値%」で値から始まるもの、「%値」で値で終わるものと指定できる  
2. 数字の比較  
Pythonと同様に「項目名 比較演算子 値」が使える  
3. AND OR検索  
「条件　AND/OR　条件」として使用する  
4. 並び替え
「ORDER BY ASC/DESC」でそれぞれ昇順、降順と並び替えることができる  
5. 範囲の設定  
「where 値 limit 個数 offset 開始位置」・・・「limit」はその後に指定した個数分レコードを取り出し、「offset」は指定した位置からレコードを取り出すことを示す  

※SQL文はフレームワークの利点からあまり好ましくない使い方であり、出来ればモデルに任せてPythonコードに統一するほうがいい  
