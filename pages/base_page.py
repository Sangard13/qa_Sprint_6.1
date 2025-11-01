import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru"
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url=""):
        self.driver.get(self.base_url + url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def send_keys_to_input(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Дождаться видимости элемента: {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться кликабельности элемента: {locator}")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Дождаться загрузки DOM")
    def wait_for_page_loaded(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = [window for window in self.driver.window_handles if window != main_window][0]
        self.driver.switch_to.window(new_window)
        return main_window

    @allure.step("Закрыть текущее окно и переключиться на основное")
    def close_and_switch_to_main_window(self, main_window):
        self.driver.close()
        self.driver.switch_to.window(main_window)

    @allure.step("Получить количество открытых окон")
    def get_window_count(self):
        return len(self.driver.window_handles)

    @allure.step("Дождаться открытия нового окна")
    def wait_for_new_window(self, timeout=10):
        initial_count = self.get_window_count()
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: len(driver.window_handles) > initial_count)

    @allure.step("Получить handle нового окна (исключая {main_window})")
    def get_new_window_handle(self, main_window):
        return [window for window in self.driver.window_handles if window != main_window][0]

    @allure.step("Переключиться на окно {window_handle}")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Дождаться URL содержащего {text}")
    def wait_for_url_contains(self, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: text in driver.current_url)

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить handle текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle