from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x) 

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2 = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

 
time.sleep(5)

