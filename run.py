#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def enable():
    while True:
        print('Вход в систему...')
        global chrome_options
        chrome_options = Options()
        chrome_options.add_argument('--log-level=OFF')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_extension('captcha.crx')
        chrome_options.add_argument('--disable-audio-output')
        global driver
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
        driver.get('https://www.vk.com/')
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
                driver.add_cookie(cookie)
        driver.refresh()
        driver.get('https://ytmonster.ru/task')
        try:
            driver.find_element_by_css_selector('#news > div > div > div > div.col-lg-2.ml-lg-auto > div > img')
            print('Вход в YtMonster не был произведен, начинаем программу заново...')
            driver.exit()
            continue
        except:
            pass
        print('Вход успешен!')
        break

def subs():
    sleep(1)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[3]/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="choseTaskType14"]/div').click()
    while True:
        sleep(6)
        while True:
            try:
                driver.find_element_by_css_selector('input.btn:nth-child(2)').click()
                break
            except:
                driver.refresh()
                sleep(1)
                driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[3]/div').click()
                sleep(1)
                driver.find_element_by_xpath('//*[@id="choseTaskType14"]/div').click()
                continue
        while True:
            try:
                handles = driver.window_handles
                driver.switch_to.window(handles[1])
                break
            except:
                driver.refresh()
                sleep(1)
                driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[3]/div').click()
                sleep(1)
                driver.find_element_by_xpath('//*[@id="choseTaskType14"]/div').click()
                sleep(1)
                driver.find_element_by_css_selector('input.btn:nth-child(2)').click()
                sleep(4)
                continue
        print('Задание началось')
        sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="join_button"]').click()
        except:
            driver.find_element_by_xpath('//*[@id="public_subscribe"]').click()
        try:
            driver.find_element_by_xpath('//*[@id="box_layer"]/div[2]/div')
            driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]').click()
            while True:
                driver.find_element_by_xpath('//*[@id="solver-button"]').click()
                sleep(5)
                try:
                    driver.find_element_by_xpath('/html/body/div/div/div[1]')
                    continue
                except:
                    break
        except:
            pass
        sleep(4)
        driver.close()
        print('Задание выполенено!')
        driver.switch_to.window(handles[0])
        
## На доработке
# def likes():
#     while True:
#         try:
#             driver.find_element_by_css_selector('input.btn:nth-child(2)').click()
#             break
#         except:
#             driver.refresh()
#             sleep(6)
#             try:
#                 driver.find_element_by_css_selector('#news > div > div > div > div.col-lg-2.ml-lg-auto > div > img')
#                 print('Вход в YtMonster не был произведен, начинаем программу заново...')
#                 driver.quit()
#                 return
#             except:
#                 pass
#     sleep(10)
#     handles = driver.window_handles
#     try:
#         driver.switch_to.window(handles[1])
#     except:
#         print('Произошла ошибка! Производим перезапуск...')
#         driver.refresh()
#         return
#     print('Задание началось')
#     sleep(1)
#     ltext = driver.find_element_by_css_selector('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/paper-tooltip/div').text()
#     if ltext == 'Больше не нравится':
#         print('Вы уже поставили лайк')
#     else:
#         driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()
#     sleep(59)
#     driver.close()
#     print('Задание выполенено!')
#     driver.switch_to.window(handles[0])
#     sleep(2)

print('Программа запускается')

enable()
while True:
    subs()
