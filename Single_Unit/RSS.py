import feedparser

#RSSのURL
RSS_URL = ''

#RSSを取得
rss = feedparser.parse(RSS_URL)
#RSSの各情報にアクセスし、タイトルとリンクを表示
for i in rss.entries:
    print(i.title,i.link)