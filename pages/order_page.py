import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить поле Имя")
    def set_field_name(self, name):
        self.send_keys_to_input(OrderPageLocators.NAME, name)

    @allure.step("Заполнить поле Фамилия")
    def set_field_surname(self, surname):
        self.send_keys_to_input(OrderPageLocators.LAST_NAME, surname)

    @allure.step("Заполнить поле Адрес")
    def set_field_address(self, address):
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)

    @allure.step("Заполнить поле Станция метро")
    def set_field_metro(self, metro_station):
        self.click_element(OrderPageLocators.METRO_STATION)
        metro_locator = (OrderPageLocators.METRO_STATION[0], OrderPageLocators.METRO_STATION[1].format(metro_station))
        self.click_element(metro_locator)

    @allure.step("Заполнить поле Телефон")
    def set_field_phone_number(self, phone_number):
        self.send_keys_to_input(OrderPageLocators.PHONE, phone_number)

    @allure.step("Заполнить первую страницу заказа")
    def fill_first_page(self, user_data):
        self.set_field_name(user_data['name'])
        self.set_field_surname(user_data['surname'])
        self.set_field_address(user_data['address'])
        self.set_field_metro(user_data['metro_station'])
        self.set_field_phone_number(user_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить поле Дата")
    def set_field_date(self, date):
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)

    @allure.step("Выбрать срок аренды: {period}")
    def set_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        period_locator = (OrderPageLocators.RENTAL_PERIOD[0], OrderPageLocators.RENTAL_PERIOD[1].format(period))
        self.click_element(period_locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def set_scooter_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)

    @allure.step("Заполнить поле Комментарий")
    def set_field_comment(self, comment):
        self.send_keys_to_input(OrderPageLocators.COMMENT, comment)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_page(self, user_data):
        self.set_field_date(user_data['date'])
        self.set_rental_period(user_data['rental_period'])
        self.set_scooter_color(user_data['color'])
        self.set_field_comment(user_data['comment'])
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Дождаться появления модального окна подтверждения")
    def wait_for_confirmation(self):
        self.wait_for_element_visible(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Нажать кнопку подтверждения заказа")
    def click_confirm_order_modal(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.get_element_text(OrderPageLocators.SUCCESS_MESSAGE)