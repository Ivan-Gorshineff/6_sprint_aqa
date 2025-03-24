from selenium.webdriver.common.by import By


class OrderPageLocators:
    '''первая страница формы'''
    FORM_TITLE_PERSONAL_DATA = (By.XPATH, ".//div[@class='Order_Header__BZXOb']")
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    SELECT_METRO_STATION = (By.XPATH, ".//div[text()='{}']")
    NUMBER_PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    '''вторая страница формы'''
    FORM_TITLE_SCOOTER_RENT = (By.XPATH, './/div[text()="Про аренду"]')
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SELECTED_DATE = (By.XPATH,
                     "//div[contains(@class, 'react-datepicker__day--selected')]")
    RENT_TIME_FIELD = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    SELECT_RENT_TIME = (By.XPATH, ".//div[text()='{}']")
    COLOR_CHECKBOX_FIELD = (By.ID, '{}')
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # окно подтверждения заказа
    ORDER_CONFIRM = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    BUTTON_CONFIRM = (By.XPATH, ".//button[text()='Да']")
    # окно оформленного заказа
    ORDER_COMPLETED = (By.XPATH, ".//div[text()='Заказ оформлен']")