from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

print('Вход в систему...')
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
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
                print('Вход в YtMonster не был произведен')
                raise SystemExit
            except:
                pass
    sleep(10)
    print('Работа началась!')
    handles = driver.window_handles
    try:
        driver.switch_to.window(handles[1])
    except:
        continue
    sleep(1)
    driver.find_element_by_css_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()
    sleep(35)
    driver.close()
    print('Задание выполенено!')
    driver.switch_to.window(handles[0])