import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData


class TestOrderScooter:

    @allure.title('Заказ самоката: {user_data[name]} через {button_type} кнопку')
    @pytest.mark.parametrize('button_type,user_data', [
        ('top', OrderData.USER_1),
        ('bottom', OrderData.USER_2)
    ])
    def test_order_scooter(self, driver, button_type, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.click_order_btn(button_type)
        order_page.fill_first_page(user_data)
        order_page.fill_second_page(user_data)
        order_page.wait_for_confirmation()
        order_page.click_confirm_order_modal()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.click_order_btn("top")
        main_page.click_scooter_logo()
        assert main_page.is_main_page()

    @allure.title("Проверка перехода по логотипу Яндекса на главную Дзен")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        # УБИРАЕМ вызов close_modal_window() - он может вызывать появление модального окна
        # main_page.close_modal_window()  # ЗАКОММЕНТИРОВАТЬ эту строку!

        main_window = main_page.get_current_window_handle()

        # Кликаем на логотип
        main_page.click_yandex_logo()

        # Ждем новое окно и переключаемся
        main_page.wait_for_new_window()
        new_window = main_page.get_new_window_handle(main_window)
        main_page.switch_to_window(new_window)

        # Ждем загрузки Дзен
        main_page.wait_for_url_contains("dzen.ru")

        # Получаем финальный URL
        current_url = main_page.get_current_url()

        # Возвращаемся
        main_page.close_current_window()
        main_page.switch_to_window(main_window)

        # Проверяем переход на Дзен
        assert "dzen.ru" in current_url, f"Ожидался переход на dzen.ru, но получен: {current_url}"