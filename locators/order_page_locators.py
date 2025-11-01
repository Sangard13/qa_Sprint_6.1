from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница заказа
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Исправлено с LAST_NAME
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__row')]")  # Упрощенный локатор
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

    # Модальные окна
    CONFIRM_MODAL = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Сообщение об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")