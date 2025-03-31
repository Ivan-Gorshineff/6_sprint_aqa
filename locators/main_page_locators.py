from selenium.webdriver.common.by import By


class MainPageLocators:

    ACCORDION_LIST = (By.CLASS_NAME, 'accordion')
    ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Home")]//button[text()="Заказать"]')

    QUESTION_1 = (By.ID, 'accordion__heading-0')
    QUESTION_2 = (By.ID, 'accordion__heading-1')
    QUESTION_3 = (By.ID, 'accordion__heading-2')
    QUESTION_4 = (By.ID, 'accordion__heading-3')
    QUESTION_5 = (By.ID, 'accordion__heading-4')
    QUESTION_6 = (By.ID, 'accordion__heading-5')
    QUESTION_7 = (By.ID, 'accordion__heading-6')
    QUESTION_8 = (By.ID, 'accordion__heading-7')

    ANSWER_1 = (By.CSS_SELECTOR, '#accordion__panel-0 p')
    ANSWER_2 = (By.CSS_SELECTOR, '#accordion__panel-1 p')
    ANSWER_3 = (By.CSS_SELECTOR, '#accordion__panel-2 p')
    ANSWER_4 = (By.CSS_SELECTOR, '#accordion__panel-3 p')
    ANSWER_5 = (By.CSS_SELECTOR, '#accordion__panel-4 p')
    ANSWER_6 = (By.CSS_SELECTOR, '#accordion__panel-5 p')
    ANSWER_7 = (By.CSS_SELECTOR, '#accordion__panel-6 p')
    ANSWER_8 = (By.CSS_SELECTOR, '#accordion__panel-7 p')

