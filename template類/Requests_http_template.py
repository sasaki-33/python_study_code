#外部ライブラリrequestsの使用
import requests

#標準ライブラリhttp.clientの使用
import http.client

#ページ内容の取得
response = requests.get('ページのURLの記入')
text = response.text
#ページ内容の表示
print(text)

#ページ内容の取得
conn = http.client.HTTPSConnection('ページのURLの記入')
conn.request('GET','/downloads/')
response = conn.getresponse()
text = response.read().decode('UTF-8')

#ページ内容の表示
print(text)
conn.close()