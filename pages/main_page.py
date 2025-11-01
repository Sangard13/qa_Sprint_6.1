import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open("/")
        self.wait_for_page_loaded()

    @allure.step("Нажать на кнопку 'Заказать' в {button_type}")
    def click_order_btn(self, button_type):
        if button_type == "top":
            self.scroll_to_element(MainLocators.HEADER_ORDER_BUTTON)
            self.wait_for_element_visible(MainLocators.HEADER_ORDER_BUTTON)
            self.click_element(MainLocators.HEADER_ORDER_BUTTON)
        else:
            self.scroll_to_element(MainLocators.FOOTER_ORDER_BUTTON)
            self.wait_for_element_visible(MainLocators.FOOTER_ORDER_BUTTON)
            self.click_element(MainLocators.FOOTER_ORDER_BUTTON)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainLocators.YANDEX_LOGO)

    @allure.step("Нажать на вопрос с индексом {index}")
    def click_question(self, index):
        question_locator = (MainLocators.QUESTION[0], MainLocators.QUESTION[1].format(index))
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        self.wait_for_element_visible((MainLocators.ANSWER[0], MainLocators.ANSWER[1].format(index)))

    @allure.step("Получить текст ответа для вопроса {index}")
    def get_answer_text(self, index):
        answer_locator = (MainLocators.ANSWER[0], MainLocators.ANSWER[1].format(index))
        return self.get_element_text(answer_locator)

    @allure.step("Проверить, что текущая страница - главная")
    def is_main_page(self):
        return self.driver.current_url == self.base_url + "/"

    @allure.step("Проверить, что URL содержит 'dzen.ru'")
    def is_dzen_page(self):
        return "dzen.ru" in self.driver.current_url

    @allure.step("Закрыть модальное окно на главной странице")
    def close_modal_window(self):
        """Закрывает возможные модальные окна на главной странице"""
        modal_selectors = [
            (By.XPATH, "//button[contains(@class, 'Modal_Close')]"),
            (By.XPATH, "//button[contains(@class, 'modal__close')]"),
            (By.XPATH, "//button[@aria-label='Закрыть']"),
            (By.CSS_SELECTOR, "[data-testid='modal-close']"),
        ]

        for selector in modal_selectors:
            try:
                self.click_element(selector)
                allure.attach(f"Закрыто модальное окно с селектором: {selector}", "Успех")
                return True
            except:
                continue

        allure.attach("Модальные окна не найдены", "Информация")
        return False