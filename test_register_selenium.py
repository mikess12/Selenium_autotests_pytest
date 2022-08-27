from selenium import webdriver
from selenium.webdriver import Keys
import time
import allure

def test_setup():
    global browser
    browser = webdriver.Chrome("C:\\Users\\trcmi\\Desktop\\Testing\\Medani\\sts_tests\\chromedriver.exe")

@allure.severity(allure.severity_level.BLOCKER)
def test_register():
    browser.get('https://synctoskill.com/')
    browser.maximize_window()
    browser.find_elements("xpath", '//a[@class="nav-link text-dark"]')[1].click()
    browser.find_elements("xpath", '//input[@class="form-control"]')[0].send_keys('Mikhail25')
    browser.find_element("name", 'Email').send_keys('mike32324@gmail.com')
    browser.find_element("name", 'Password').send_keys('Merinda4++')
    browser.find_element("name", 'PasswordConfirmation').send_keys('Merinda4++')
    browser.find_element("name", 'Phone').send_keys('7(926)769-63-69')
    browser.find_element("name", 'Address').send_keys('Bali House23')
    browser.find_element("xpath", '//input[@value="Sign Up"]').click()

    time.sleep(7)
    browser.close()
