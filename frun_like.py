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
    chrome_options.add_argument('--disable-audio-output')
    driver = webdriver.Chrome(options=chrome_options)
    with open('pass_yt.txt', 'r') as file:
        passyt = file.read()
    with open('log_yt.txt', 'r') as file:
        logyt = file.read()
    logyt = logyt.strip()
    passyt = passyt.strip()
    driver.get('https://ytmonster.ru/')
    while True:
        try:
            driver.find_element_by_css_selector('body > table > tbody > tr > td > div.cf-browser-verification.cf-im-under-attack')
            sleep(2)
        except:
            break
    sleep(1)
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a').click()
            break
        except:
            driver.refresh()
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
    driver.get('https://ytmonster.ru/task')
    try:
        driver.find_element_by_css_selector('#news > div > div > div > div.col-lg-2.ml-lg-auto > div > img')
        print('Вход в YtMonster не был произведен, начинаем программу заново...')
        driver.quit()
        return
    except:
        pass
    print('Вход успешен!')
    sleep(2)
    while True:
        while True:
            try:
                driver.find_element_by_css_selector('input.btn:nth-child(2)').click()
                break
            except:
                driver.refresh()
                sleep(6)
                try:
                    driver.find_element_by_css_selector('#news > div > div > div > div.col-lg-2.ml-lg-auto > div > img')
                    print('Вход в YtMonster не был произведен, начинаем программу заново...')
                    driver.quit()
                    return
                except:
                    pass
        sleep(10)
        print('Задание началось')
        handles = driver.window_handles
        try:
            driver.switch_to.window(handles[1])
        except:
            print('Произошла ошибка! Производим перезапуск...')
            driver.quit()
            return
        print('Задание началось')
        sleep(1)
        try:
            driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-default-active > a')
            print('Лайк уже поставлен! Ждем 35 сек. и идем дальше.')
            sleep(35)
            driver.close()
            driver.switch_to.window(handles[0])
            continue
        except:
            pass
        driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()
        sleep(40)
        driver.close()
        print('Задание выполенено!')
        driver.switch_to.window(handles[0])
        sleep(2)

while True:
    func()
