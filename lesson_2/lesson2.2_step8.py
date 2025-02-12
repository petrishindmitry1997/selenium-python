from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Dmitriy')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Lastname')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('email@test.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
