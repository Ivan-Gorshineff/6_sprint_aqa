from selenium.webdriver.common.by import By


class BasePageLocators:

    SCOOTER_BUTTON = (By.XPATH, ".//a[@href='/']")
    LOGO_BUTTON = (By.XPATH, ".//a[@href='//yandex.ru']")
    HEADER_ORDER_BUTTON = (By.XPATH, './/button[text()="Заказать"]')
