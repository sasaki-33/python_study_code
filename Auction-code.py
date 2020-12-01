from selenium import webdriver
from time import sleep

word = input('検索したい商品を入力して下さい。')

driver = webdriver.Chrome('')

driver.get('https://www.amazon.co.jp/')
sleep(2)

kensaku = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
kensaku.send_keys(word)

botton = driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input')
botton.click()
