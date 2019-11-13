from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x) 

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

option2 = browser.find_element_by_css_selector("[for='robotsRule']")
option2.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

webdriver.quit()


