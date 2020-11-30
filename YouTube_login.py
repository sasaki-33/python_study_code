from selenium import webdriver
import time
driver = webdriver.Chrome('webdriverのファイル')

#YouTubeへ
driver.get('https://www.youtube.com/')
time.sleep(5)

#ログインボタンのXpathを取得、クリック
i1 = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
i1.click()
time.sleep(3)

#メールアドレス入力の要素を取得、書き込み
i2 = driver.find_element_by_name('identifier')
i2.send_keys('メールアドレス')
#次へのボタンのXpathを取得

i3 = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
i3.click()
#パスワードの要素を取得、以下同様