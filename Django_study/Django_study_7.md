# Django学習記録(day7)
## 管理ツールの使い方
まず、管理ユーザを作成する  
ターミナルで、python manage. py createsuperuserより、必要な情報を登録する  
次に、モデルを管理ツールで利用するために、アプリケーションのadmin. pyに必要な情報を登録する  
```python
from django.contrib import admin
from .models import Human

admin.site.register(Human)
```  
これにより、Humanモデルクラスが管理ツールで使用できるようになった  
そしてhttp://localhost:8000/admin で管理ツールにログインする  
管理ツールで適用なレコードを追加する

## レコード取得
管理ツールで作成したレコードの情報をviews. pyを利用してレコード内容を表示する
views. pyを編集し、
```python
from django.shrtcuts import render
from django.http import HttpResponse
from .models import Human

def index(request):
    data = Human.objects.all()
    params = {
        'title':'hello',
        'msg':'all human',
        'data':data,
    }
    return render(request, 'test/index.html', params)
```  
* 「all」は、objectsに存在するメソッドで、テーブルにあるレコードを、モデルのインスタンスのセットとしてまとめている  

※コード内にエラーが発生し、Class '~~~' has no 'objects' memberpylint(no-member)となった  
モデルクラスには標準で、objectsという属性を持つはずなのでmodels. pyで
```python
objects = models.Manager()
```
を追加し、クラス属性をobjectsという変数を格納することでエラーを解決する  
(objectsという名前の変数にManagerクラスのインスタンスを格納する)

## objectsについて
objectsはManagerクラスのインスタンスのことで、Managerクラスとは「データベースクエリ」を操作するためのクラスである  
「データベースクエリ」とは、データベースに対して様々な要求をするためのもので、「SQL」でデータベースへ問い合わせる内容を記述した命令文を「クエリ」という  
Managerクラスでは、メソッド内で、クエリを作成し、データベースに問い合わせをし、その結果であるレコードを取得する  
つまりManagerクラスは、Pythonのメソッドをデータベースクエリに翻訳して実行するものといえる  
