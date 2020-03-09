from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def login():
    print('Введите сначала ваш логин от YTMonster, а потом пароль')
    passyt = input('Логин: ')
    logyt = input('Пароль: ')
    with open('pass_yt.txt', 'w') as file:
        file.write(passyt)
    with open('log_yt.txt', 'w') as file:
        file.write(logyt)
    print('Отлично! Теперь, войдите вручную в ваш гугл аккаунт (Сейчас появится браузер)')
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    input('Войдите как обычно, а потом нажмите Enter. Если вам пишут, что вход небезопасен, то создайте новый аккаунт.')
    pickle.dump(driver.get_cookies(), open("cookiesgoogle.pkl", "wb"))
    print('Вход удался!')
    driver.quit()

def likes():
    print('Вход в систему...')
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    with open('pass_yt.txt', 'r') as file:
        passyt = file.read()
    with open('log_yt.txt', 'r') as file:
        logyt = file.read()
    logyt = logyt.strip()
    passyt = passyt.strip()
    driver.get('https://ytmonster.ru/')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a').click()
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/input[1]').send_keys(logyt)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/input[2]').send_keys(passyt)
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
                    driver.find_element_by_css_selector('#home > div > div.header-info > div.header-bigPla')
                except:
                    print('Вход на YtMonster не был произведен!')
                    SystemExit()
        sleep(5)
        print('Работа началась!')
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()
        sleep(35)
        driver.close()
        print('Задание выполенено!')
        driver.switch_to.window(handles[0])

print('Вы уже входили в YtMonster и Google в данной программе?')
print('''
1. Да 
2. Нет
''')
while True:
    try:
        flogin = int(input('Введите число: '))
    except:
        print('Вы ввели литеральное значение/ничего не ввели, введите число!')
        continue
    if flogin == 1:
        try:
            print('''1. Выполнять лайки
2. Выполнять подписки (Не готово)''')
            menu_pick = int(input('Введите число: '))
            if menu_pick == 1:
                likes()
            elif menu_pick >= 1:
                print('Введите указанное число')
            elif menu_pick <= 1:
                print('Введите указанное число')
        except:
            print('Вы ввели литеральное значение/ничего не ввели, введите число!')
            continue
    elif flogin == 2:
            login()
