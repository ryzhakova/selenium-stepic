from selenium import webdriver
import time
import math
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x) 

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)



button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

 
time.sleep(5)

browser.quit()