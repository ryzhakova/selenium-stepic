from selenium import webdriver
import time
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

print(os.path.abspath(__file__)) 
print(os.path.abspath(os.path.dirname(__file__)))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 



input1 = browser.find_element_by_css_selector("[name='firstname']")
input1.send_keys("Kate")

input2 = browser.find_element_by_css_selector("[name='lastname']")
input2.send_keys("Ryz")

input3 = browser.find_element_by_css_selector("[name='email']")
input3.send_keys("email@domain.com")

inpfile = browser.find_element_by_css_selector("[type='file']")
inpfile.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

 
time.sleep(5)

browser.quit()