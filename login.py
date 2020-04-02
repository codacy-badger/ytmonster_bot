#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


print('Введите сначала ваш логин от YTMonster, а потом пароль')
logyt = input('Логин: ')
passyt = input('Пароль: ')
with open('pass_yt.txt', 'w') as file:
    file.write(passyt)
with open('log_yt.txt', 'w') as file:
    file.write(logyt)
print('Отлично! Теперь, войдите вручную в ваш ВК аккаунт (Сейчас появится браузер)')
chrome_options = Options()
chrome_options.add_argument('./webdriver')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://vk.com/")
input('Войдите как обычно, а потом нажмите Enter.')
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
print('Вход удался!')
driver.quit()
