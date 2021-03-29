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

## レコードの表示  
index.htmlを編集し、
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{msg|sage}}<p>
    <table>
        <tr>
            <th>ID</th>
            <th>NAME<th>
            <th>GENDER</th>
            <th>MAIL<th>
            <th>AGE</th>
            <th>BIRTHDAY</th>
        </tr>
    {% for item in data %}
        <tr>
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
            <td>{% if item.gender == False %}male{% endif %}
                {% if item.gender == True %}female{% endif %}</td>
            <td>{{item.mail}}</td>
            <td>{{item.age}}</td>
            <td>{{item.birthday}}</td>
        </tr>
    {% endfor %}
    </table>
</body>
</html>
```
* {% for item in data %}で、viewsから渡されたdataのオブジェクトを順に取り出し、変数itemに入れる繰り返し文である  
{% endfor %}で繰り返し範囲の終了を表す  

urls. pyを編集し、
```python
from django.urls import path
from . import views

urlpattrens = [
    path('', views.index, name='index'),
]
```
これで、データベースからobjects.all()で取り出した情報をviewsを介し、index.htmlに変数を渡すことで、その情報をブラウザ上で表示することができる

## 特定のレコードのみ表示
IDを入力するフォームを用意し、そのIDと一致するレコードを取り出す  
特定のレコードを取得するために、「get」というメソッドを使用する  
フォームを用意するために、TestFormを編集し、  
```python
from django import forms

class TestForm(forms.Form):
    id = forms.IntegerField(label='ID')
```  
views. pyを編集し、  
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Human
from .forms import TestForm

def index(request):
    params = {
        'title':'hello',
        'msg':'kensaku',
        'form':TestForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        i = request.POST['id']
        item = Human.objects.get(id=i)
        params['data'] = [item]
        params['form'] = TestForm(request.POST)
    else:
        params['data'] = Human.objects.all()
    
    return render(request, 'test/index.html', params)
```
* 変数「i」に、POSTにより取得したキー値が「id」である値を格納し、さらにその値と一致するレコードを変数itemに格納している  
変数「item」に格納された値は、一つのモデルのインスタンスであり、all()で得られたようなインスタンスのセットでは無いので、セットにした[ item ]を、params[ 'data' ]に格納している  
これにより、index.htmlの{% for item in data %}が実行可能になる  

index.htmlも編集し、  
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{msg|safe}}</p>
    <form action="{% url 'index' %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="click">
    </form>
    <hr>
    <table>
    <tr>
        <th>ID</th>
        <th>NAME</th>
        <th>GENDER</th>
        <th>MAIL</th>
        <th>AGE</th>
        <th>BIRTHDAY</th>
    </tr>
    {% for item in data %}
    <tr>
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
        <td>{% if item.gender == False %}male{% endif %}
            {% if item.gender == True %}female{% endif %}</td>
        <td>{{item.mail}}</td>
        <td>{{item.age}}</td>
        <td>{{item.birthday}}</td>
    </tr>
    {% endfor %}
    </table>
</body>
</html>
```  
## 補足
html内のタグについての補足  
* < p >タグは段落を指定するタグで< p >~</ p >が一つの段落であることを表す
* < hr >タグは水平の横線を引くためのタグ
* < tr >タグは表の行部分を指定するタグで< tr >~</ tr >で表の行部分を指定する  
< th >や< td >で表題や縦軸を指定してセルを定義する  
* < th >はTable Headerの略で、セルの内容が見出しとなるヘッダセルを作成する
* < td >はTable Dataの略で、セルの内容がデータであるときに使用する