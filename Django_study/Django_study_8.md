# Django学習記録(day8)
## CRUDについて
データベースを利用する基本的な機能にCRUDというものがある  
Create・・・新たにレコードを作成し、テーブルに保存する  
Read・・・テーブルからレコードを取得する(all(),get())  
Update・・・テーブルに存在するレコードの内容を変更する  
Delete・・・テーブルに存在するレコードの内容を削除する  

## Createを実行
Create、レコードを追加するには、フォームを送信してレコードを追加しテーブルに保存する方法を取る    
このCreateではforms.Formを使用する方法と、ModelFormを使用する方法がある  

### forms.Formを使用する方法
フォームを表示するためのcreate.htmlと、レコード内容を表示するindex.htmlを用意する  
create.htmlを新規作成し、  
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <form action="{% url 'create' %}" method="post">
        {% csrf_token %} 
        {{ form.as_p }}
        <input type="submit" value="click">
    </form>
</body>
</html>
```  

そしてforms. pyのTestFormクラスを修正し、
```python
from django import forms

class TestForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
```  
views. pyを編集し、
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Human
from .forms import TestForm

# index.htmlの表示内容を定義
def index(request):
    data = Human.objects.all()
    params = {
        'title':'all data',
        'data':data,
    }
    return render(request, 'test/index.html', params)
# create.htmlの表示内容を定義
def create(request):
    params = {
        'title':'your data',
        'form':TestForm(),
    }
    # POST送信された場合
    if (request.method == 'POST'):
        # 変数にPOST送信された値を格納
        name = request.POST['name']
        mail = request.POST['mail']
        gender = request.POST['gender']
        age = request.POST['age']
        birth = request.POST['birthday']
        # Humanクラスのインスタンスを作成する
        human = Human(name=name,mail=mail,gender=gender,age=age,birthday=birth)
        # インスタンス(レコード)を保存
        human.save()
        # POST送信された場合、/testにリダイレクトする
        return redirect(to='/test')
    # POST送信でない場合、通常のフォーム画面を表示
    return render(request, 'test/create.html', params)
```  
以上
### ModelFormを使用する方法
forms. pyに新たにクラスを追加する
```python
from django import forms
from .models import Human

class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['name','mail','gender','age','birthday']
```  
views. pyのcreate関数を編集し、
```python
from .forms import HumanForm
# 省略
def create(request):
    params = {
        'title':'your data',
        'form':HumanForm(),
    }
    if (request.method == 'POST'):
        # Humanクラスのインスタンスを作成
        obj = Human()
        # 引数に、POST送信された全ての情報と、Humanクラスのインスタンスを指定し、HumanFormクラスのインスタンスを作成
        human = HumanForm(request.POST, instance = obj)
        # インスタンス(レコード)を保存
        human.save()
        # /testにリダイレクトする
        return redirect(to='/test')
    return render(request, 'test/create.html', params)
```  
* HumanFormにて、Modelとrequest.POSTの情報を、HumanFormにて一つにまとめ、レコードを作成している   

以上

## update(更新)を行う
Humanインスタンスを使用して情報を上書きし、HumanFormでレコードを作成し、保存すれば、更新ができる  
urls. pyを編集し、  
```python
urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('edit/<int:num>',views.edit,name='edit')
]
```
* これにより、edit/ID番号にアクセスした時、viewsのedit関数を実行できる  


次に、/testにアクセスした時に、レコード内容の表示と同時に、更新できるリンクを作成しておく(index.html)
```html
<td><a href="{% url 'edit' item.id %}">Edit</a></td>
```  

これにより、/edit/ID番号にアクセスされ、urlpatternsに従いedit関数が実行されるので、viewsにedit関数を作成する
```python
# urlpatternsにより、ID番号もnumとして受け取る
def edit(request,num):
    # IDと一致するレコードオブジェクトのみ変数に格納
    obj = Human.objects.get(id=num)
    # POST送信(更新された情報)ならば
    if (reequest.method == 'POST'):
        # レコードの作成
        human = HumanForm(request.POST,instance=obj)
        # 保存
        human.save()
        # /testにリダイレクトする
        return redirect(to='/test')
    params = {
        'title':'edit your data',
        'id':num,
        'form':HumanForm(instance=obj),
    }
    return render(request, 'test/edit.html', params)
```  

最後に値が渡されるedit.htmlを新規作成する
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <form action="{% url 'edit' id %}" method="post">
    {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr><th><td>
            <input type="submit" value="click">
        </td></th></tr>
        </table>
    </form>
</body>
</html>
```
* action="{% url 'edit' id %}"とすることで、編集するID番号ごとにtest/edit/ID番号のアドレスが設定される

## Delete(削除)を行う
削除するモデルのインスタンスを取得し、そのインスタンスの「delete」メソッドを実行すれば、削除できる
urls. pyのurlpatternsを編集し、  
```python
path = ('delete/<int:num>', views.delete, name='delete'),
```  
を追加し、/delete/ID番号にアクセスした時に、delete関数を実行するようにする  
また、更新と同様にindex.htmlに、Deleteと書かれたリンクを追加する  
```html
<td><a href="{% url 'delete' item.id %}">Delete</a></td>  
```  
/delete/ID番号のURLにアクセスした時に、delete関数を実行するようにしたので、  
views. pyにdelete関数を追加し、  
```python
# urlpatternから、ID番号も引数として取得
def delete(request,num):
    # IDと一致するモデルのインスタンスを取得し、変数に格納
    human = Human.objects.get(id=num)
    if (request.method == 'POST'):
        # POST送信ならば、そのインスタンスを削除する
        human.delete()
        # /testにリダイレクトする
        return redirect(to='/test')
    params = {
        'title':'delete this data',
        # idは受け取ったID番号
        'id':num,
        # 該当インスタンスを渡す
        'obj':human,
    }
    return render(request, 'test/delete.html', params)
```  

削除する場合のhtmlを新規作成する  
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <table>
        <tr><th>ID</th><td>{{obj.id}}</td></tr>
        <tr><th>Name</th><td>{{obj.name}}</td></tr>
        <tr><th>Gender</th><td>
        {% if obj.gender == False %}male{% endif %}
        {% if obj.gender == True %}female{% endif %}</td></tr>
        <tr><th>Email</th><td>{{obj.mail}}</td></tr>
        <tr><th>Age</th><td>{{obj.age}}</td></tr>
        <tr><th>Birth</th><td>{{obj.birthday}}</td></tr>
        <form action="{% url 'delete' id %}" method = "post">
        {% csrf_token %}
        <tr><th></th><td>
            <input type="submit" value="delete"></td></tr>
        </form>
    </table>
</body>
</html>
```  
以上
