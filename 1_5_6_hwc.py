from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
# Ваш код, который заполняет обязательные поля
field1 = browser.find_element_by_xpath("//input[@class='form-control first']").send_keys('dwede')
field2 = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']").send_keys('wfwefewfw')
field3 = browser.find_element_by_xpath("//input[@placeholder = 'Введите Email']").send_keys('wfwefewfw')
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайт
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

