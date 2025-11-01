from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница заказа
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_STATION = (By.XPATH, "//div[@class='select-search__select']//button[contains(., '{}')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница заказа
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_OPTION = (By.XPATH, "//div[text()='{}']")
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")

    # Модальные окна
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_TITLE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")