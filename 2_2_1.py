from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
num2 = browser.find_element_by_id("num2")

res = str(int(num1.text)+int(num2.text))

option1 = browser.find_element_by_css_selector("[value='"+res+"']")
option1.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(10)

browser.quit()


