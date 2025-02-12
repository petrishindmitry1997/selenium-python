import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException

# Укажите свои данные для авторизации
LOGIN = "petrishin_dmitriy@mail.ru"
PASSWORD = "7ujm8ik9ol00pp"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ]
    @pytest.mark.parametrize("links", links)
    def test_stepik(self, browser, links):
        browser.get(links)

        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        login_button.click()

        # Вводим логин
        email_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_login_email"))
        )
        email_input.send_keys(LOGIN)

        # Вводим пароль
        password_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_login_password"))
        )
        password_input.send_keys(PASSWORD)
        browser.implicitly_wait(10)  # Corrected line
        password_input.send_keys(Keys.RETURN)
        try:
            # Если кнопка "Решить снова" есть
            browser.implicitly_wait(10)
            button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
            button_again.click()

            # Если кнопки "Решить снова" нет
        except NoSuchElementException:
            print('Кнопка "Решить снова" отсутствует')

        finally:
            # Находим поле ввода ответа
            time.sleep(10)
            input_answer = browser.find_element(By.TAG_NAME, 'textarea')
            input_answer.clear()

            # Вычисляем ответ
            answer = math.log(int(time.time()) + 2.0)
            answer_text = str(answer)

            # Вводим и отправляем ответ
            input_answer.send_keys(answer_text)
            time.sleep(5)
            button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
            button_send.click()

            # Проверяем ответ
            browser.implicitly_wait(10)
            answer_feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
            assert answer_feedback.text == "Correct!", f"{answer_feedback.text}"

if __name__ == "__main__":
    pytest.main()
