from selenium.webdriver.common.by import By


class BasePageLocators:

    SCOOTER_LOGO_BUTTON = (By.XPATH, ".//a[@href='/']")
    YANDEX_LOGO_BUTTON = (By.XPATH, ".//a[@href='//yandex.ru']")
    HEADER_ORDER_BUTTON = (By.XPATH, './/button[text()="Заказать"]')
