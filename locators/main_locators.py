from selenium.webdriver.common.by import By


class MainLocators:
    # Кнопки заказа
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    FOOTER_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")

    # Вопросы о важном
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")