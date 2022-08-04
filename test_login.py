from selenium import webdriver
from selenium.webdriver import Keys
import time

def test_setup():
    global browser
    browser = webdriver.Chrome("C:\\Users\\trcmi\\Desktop\\Testing\\Medani\\sts_tests\\chromedriver.exe")

def test_login():
    browser.get('https://sandbox.synctoskill.com/')
    browser.maximize_window()
    browser.find_elements("xpath", '//a[@class="nav-link text-dark"]')[0].click() #кликаем на кнопку логина
    browser.find_element("name", 'Email').send_keys('sfanat@yandex.ru')   #вводим почту
    browser.find_element("name", 'Password').send_keys('Merinda4+')
    #browser.find_element("xpath", '//input[@class="button"]').click()
    browser.find_element("xpath", '//input[@value="Sign In"]').click()
    browser.find_element("xpath", '//a[@href="/Account/Profile"]').get_attribute('text').find("Mikhail Filimonov")
def test_search():
    browser.find_element("xpath", '//input[@class ="searchBar"]').send_keys('avocado')  #найти строку поиска и вставить туда слово авокадо
    browser.find_element("xpath", '//input[@class ="searchBar"]').send_keys(Keys.ENTER) #нажать клавишу Enter
    # browser.get_screenshot_as_file('3.png') 
    time.sleep(5)
    browser.close()










