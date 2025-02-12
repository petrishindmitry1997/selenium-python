from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your first name']")
    input1.send_keys("Dmitriy")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your last name']")
    input2.send_keys("Petrishin")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[placeholder='Input your email']")
    input3.send_keys("email@mail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your phone:']")
    input4.send_keys("Saint-Petersburg")
    input5 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your address:']")
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
