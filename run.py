#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


def enable():
    while True:
        display = Display(visible=0, size=(400, 300))
        display.start()
        print('Вход в систему...')
        global chrome_options
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
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
                driver.find_element_by_css_selector(
                    'body > table > tbody > tr > td > div.cf-browser-verification.cf-im-under-attack')
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
            continue
        except:
            pass
        print('Вход успешен!')
        break

def subs():
    try:
        driver.find_element_by_xpath('//*[@id="choseTaskType2"]/div').click()
    except:
        pass
    while True:
        while True:
            try:
                driver.find_element_by_css_selector('input.btn:nth-child(2)').click()
                break
            except:
                driver.refresh()
                try:
                    driver.find_element_by_xpath('//*[@id="choseTaskType2"]/div').click()
                except:
                    print('Вход в YtMonster не был произведен, начинаем программу заново...')
                    driver.quit()
                    enable()
                sleep(6)
        sleep(10)
        handles = driver.window_handles
        print(handles)
        try:
            driver.switch_to.window(handles[1])
        except:
            driver.find_element_by_xpath('//*[@id="choseTaskType1"]/div').click()
            print('Задания пока недоступны. Выполняем лайки.')
            return
        print('Задание началось')
        sleep(1)
        try:
            subtext = driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > paper-button > yt-formatted-string').text
        except:
            pass
        if subtext == 'Вы подписаны':
            print('Вы уже подписани')
            continue
        else:
            pass
        try:
            driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > paper-button').click()
        except:
            print("Подписка уже была выполнена")
        sleep(59)
        driver.close()
        print('Задание выполенено!')
        driver.switch_to.window(handles[0])
        sleep(2)

def likes():
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
    handles = driver.window_handles
    try:
        driver.switch_to.window(handles[1])
    except:
        print('Произошла ошибка! Производим перезапуск...')
        driver.refresh()
        return
    print('Задание началось')
    sleep(1)
    ltext = driver.find_element_by_css_selector('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/paper-tooltip/div').text()
    if ltext == 'Больше не нравится':
        print('Вы уже поставили лайк')
    else:
        driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()
    sleep(59)
    driver.close()
    print('Задание выполенено!')
    driver.switch_to.window(handles[0])
    sleep(2)

print('Программа запускается')

enable()
while True:
    subs()
    for i in range(10):
        likes()
