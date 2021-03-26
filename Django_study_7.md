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
コード内にエラーが発生し、Class '~~~' has no 'objects' memberpylint(no-member)となった  
モデルクラスには標準で、objectsという属性を持つはずなのでmodels. pyで
```python
objects = models.Manager()
```
を追加し、再度認識させたところ、エラー表示が無くなった