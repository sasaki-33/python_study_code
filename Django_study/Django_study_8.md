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
    return render(request, 'hello/index.html', params)
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
        # POST送信された場合、/helloにリダイレクトする
        return redirect(to='/hello')
    # POST送信でない場合、通常のフォーム画面を表示
    return render(request, 'hello/create.html', params)
```  
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
        # /helloにリダイレクトする
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)
```  
* ここでは、Modelとrequest.POSTの情報を、HumanFormにて一つにまとめ、レコードを作成している  
