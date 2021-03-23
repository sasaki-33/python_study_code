# Django学習記録(day5)
## ビュー関数のクラス化
「views. py」のビュー関数をクラス化することで、処理を単純化できる

## viewクラスの作成
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import TestForm


class TestView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Test'
            'msg':'your data'
            'form':TestForm()
        }
    
    def get(self, request):
        return render(request, 'test/index.html', self.params)

    def post(self, request):
        msg = 'you are, <b>' + request.POST['name'] + \
            'and' + request.POST['age'] + 'years old' + \
                '</b>' + '<br>mail is ' + request.POST['mail'] + '</br>'
        self.params['msg'] = msg
        self.params['form'] = TestForm(request.POST)
        return render(request, 'test/index.html', self.params)
```
* TemlateViewクラスを継承し、クラスを定義する  
templateViewクラスはビューを扱うViewクラスの派生クラス
* クラス内にGETを扱うメソッド、POSTを扱うメソッドを作成する
  
「urls. py」を編集し、
```python
from django.conf.urls import url
from .views import TestView

ulspatterns = [
    url(r'', TestView.as_view(), name = 'index')
]
```
* 今までは「view. py」内の関数を作るたびにパスとの紐づけが必要だったが、クラスを作ることで「urls. py」のパスを一つ定義するだけで済む  