import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_button = browser.find_element(By.LINK_TEXT, num)
    link_button.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Dmitriy")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrishin")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Saint-Petersburg")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла