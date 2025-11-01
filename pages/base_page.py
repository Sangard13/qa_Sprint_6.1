import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru"
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def open(self, url=""):
        self.driver.get(self.base_url + url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def send_keys_to_input(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Проскроллить к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента {locator}")
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить handle текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить список всех window handles")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Дождаться нового окна")
    def wait_for_new_window(self):
        current_handles = self.get_window_handles()
        self.wait.until(lambda driver: len(driver.window_handles) > len(current_handles))

    @allure.step("Получить handle нового окна (исключая {main_window})")
    def get_new_window_handle(self, main_window):
        return [window for window in self.driver.window_handles if window != main_window][0]

    @allure.step("Переключиться на окно {window_handle}")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Дождаться URL содержащего {text}")
    def wait_for_url_contains(self, text):
        self.wait.until(lambda driver: text in driver.current_url)

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))