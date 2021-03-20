

# Djangoの学習記録(day2)
## アプリケーションの作成(続きから)
「test」フォルダ内の「views. py」に表示するページ情報を書く  
そして、簡単なテキストを画面に表示する処理を書いてみる  

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is test')
```  
* クライアントからのアクセスにレスポンスする内容を管理している、HttpResponseクラスをimportしている  
* index関数の引数のrequestは、クライアントのリクエストの内容を管理している、HttpRequestクラスのインスタンスである  
* return文では、HttpResponseクラスのインスタンスを作成し、それを戻り値としてクライアントに返している  

そして、この「views. py」のindex関数を実行させるために、プロジェクト内のURL情報を管理している「urls. py」にこの関数を登録する必要がある。  
「django_app」内の「urls. py」を開き、  
```python
from django.contrib import admin
from django.urls import path
import test.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test.views.index),
]
```
* 追加したpath関数は、path( アクセスするアドレス, 呼び出す関数 )で実行する  

これで、「urls. py」にtestアプリケーションの「views. py」のindex関数が登録されたので、'~/test/'にアクセスすると、index関数が実行されるようになる  
  
しかし、(day1)で記述したように、アプリケーションは複数のMVC(MTV)で構成されるので、プロジェクト内のurls. py一つで複数のアプリケーションのURL情報を管理しているとアプリケーションを作成するごとに「django_app」内の「urls. py」を書き足す必要がある。  
もし、一つのプロジェクトに複数のアプリケーションを置く場合は、  testフォルダ内に新たな「urls. py」を作成し、  
```python
from django.urls import path
from . import views

urlpatterns = [
    path = ('', views.index)
]  
```
* パス名を空にしているが、この「urls. py」がtestフォルダ内にあるので、このパスは「~/test/」以降のパスを指定することになっている  

「django_app」の「urls. py」を編集し、  
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('test.urls')),
]
```
* これにより~/test/以降のパスは「test」フォルダ内の「urls. py」が読み込まれることになる  

## 補足
クエリパラメータを付加する場合の処理は、「test/?mag=good」とするとき、    
「test」フォルダ内の「views. py」を開き
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'msg="' + msg + '".'
    
    else:
        result = 'please send msg parament'
    
    return HttpResponse(result)
```  
* 「request」インスタンスは「GET」という属性を持つ  
この属性は、「QueryDict」という辞書型のようなプロパティである  
つまり、クライアントから送られたリクエスト内のGET属性に'msg'というキー値が存在するかどうかの判定をif文で行っている  

さらにパラメータを分かりやすくし、「test/?id=333&name=sasa」を「test/333/sasa」でアクセスできるようにするには、「test」フォルダ内の「urls. py」を編集し、  
```python
urlpatterns = [
    path = ('<int:id>/<name>/', views.index)
]  
```  
さらに、「test」フォルダ内の「views. py」を編集し、  
```python
def index(request, id, name):
    result = 'id:' + str(id) + 'name:' + name '".'
    return HttpResponse(result)
```  
* index関数の引数「id」と「name」は、「urls. py」で設定した'< int: id >/< name >/'というアドレスの「id」と「name」である  
このように、*urlpatternsで<>を使って記述した値は、そのまま呼び出される関数の引数として使用可能である  

## メモ
次はテンプレートについて学習する