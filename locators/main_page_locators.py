from selenium.webdriver.common.by import By


class MainPageLocators:

    MAIN_TITLE_SCOOTER = [By.XPATH, './/div[@class="Home_Header__iJKdX"]']
    ACCORDION_LIST = [By.CLASS_NAME, 'accordion']
    ACCORDION_QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    ACCORDION_ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]
    FOOTER_ORDER_BUTTON = [By.XPATH, './/div[@class="Button_Button__ra12g Button_Middle__1CSJM"]//button[text()="Заказать"]']