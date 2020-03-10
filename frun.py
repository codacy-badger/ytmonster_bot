#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def func():
    print('Вход в систему...')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--enable-tab-audio-muting')
    driver = webdriver.Chrome(options=chrome_options)
    with open('pass_yt.txt', 'r') as file:
        passyt = file.read()
    with open('log_yt.txt', 'r') as file:
        logyt = file.read()
    logyt = logyt.strip()
    passyt = passyt.strip()
    driver.get('https://ytmonster.ru/')
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/input[1]').send_keys(logyt)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/input[2]').send_keys(passyt)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="booSubmit"]').click()
    sleep(5)
    driver.get('https://www.youtube.com/')
    cookies = pickle.load(open("cookiesgoogle.pkl", "rb"))
    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
            driver.add_cookie(cookie)
    driver.refresh()
    print('Вход успешен!')
    driver.get('https://ytmonster.ru/task')
    sleep(2)
    while True:
        while True:
            try:
                driver.find_element_by_css_selector('input.btn:nth-child(2)').click()
                break
            except:
                driver.refresh()
                sleep(2)
                try:
                    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[1]/a')
                except:
                    print('Вход в YtMonster не был произведен, начинаем программу заново...')
                    driver.quit()
                    return
        sleep(10)
        print('Задание началось')
        handles = driver.window_handles
        try:
            driver.switch_to.window(handles[1])
        except:
            print('Произошла ошибка! Производим перезапуск...')
            driver.quit()
            return
        sleep(1)
        driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()
        sleep(35)
        driver.close()
        print('Задание выполенено!')
        driver.switch_to.window(handles[0])

while True:
    func()
