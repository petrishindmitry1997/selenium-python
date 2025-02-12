import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegisterPage(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

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

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should get anouther text")

        time.sleep(1)
        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

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

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1) 

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should get anouther text")

        time.sleep(1)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
