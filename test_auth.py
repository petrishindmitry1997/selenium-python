import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        # Проверяем, что поле для ответа пустое
        answer_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        # Вводим правильный ответ
        answer = str(math.log(int(time.time() + 2.0)))
        answer_field.send_keys(answer)
        time.sleep(10)

        # Нажимаем кнопку "Отправить"
        submit_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_button.click()
        time.sleep(10)
        # Проверяем текст фидбека
        feedback = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text

        assert feedback == "Correct!", f"Ожидалось, что фидбек будет 'Correct!', но получено '{feedback}'"

if __name__ == "__main__":
    pytest.main()
