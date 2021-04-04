# 検索について
## フィルターについて
モデルのobjects属性のManagerに、「フィルター」という検索に関係する機能がある  
フィルターを使い、テーブルに保存したレコードの中から条件に合致するレコードを検索することができる  

## フィルターを使用する
モデル名.objects.filter(フィルターの内容)で使用できる  
フィルターを使用するにあたり、viewsに関数を新規作成する  
まずは、urls. pyを編集し、  
```python
path('find', views.find, name = 'find'),
```  
このパスを追加し、test/findにアクセスした時に、find関数を実行するようにする  
次に、フィルターの内容を書き込むフォームを作成する  
forms. pyに以下のクラスを追加する  
```python
class FindForm(forms.Form):
    find = forms.CharField(label = 'find', required = False)
```  
* HumandFormクラスのように、forms.Formを継承し、Formクラスを作成する  

find関数を作成する
```python
# 作ったFindFormをインポート
from .forms import FindForm
# 略
def find(request):
    # POST送信されたとき
    if (request.method == 'POST'):
        # フォームのインスタンスを作成
        form = FindForm(request.POST)

        # POST送信された'find'の値を変数に格納する
        find = request.POST['find']
        # フィルターで名前を指定し、レコードを変数に格納する
        data = Human.objects.filter(name = find) # レコードの項目名 = 値

        # POST送信された時のメッセージ内容
        msg = 'result is :' + str(data.count())
    else:
        msg = 'data is ...'
        # 空フォームを表示
        form = FindForm()
        # POST送信でない場合、全てのレコードを表示
        data = Human.objects.all()
    
    params = {
        'title':'search',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'test/find.html', params)
```  

検索用のテンプレートを新規作成する  
```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{message|safe}}</p>
    <form action="{% url 'find' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <tr><th></th><td>
        <input type="submit" value="click"></td></tr>
    </form>
    <hr>
    <table>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>mail</th>
        </tr>
    {% for item in data %}
        <tr>
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
            <td>{{item.mail}}</td>
    {% endfor %}
    </table>
</body>
</html>
```  
これで、検索が可能になる
