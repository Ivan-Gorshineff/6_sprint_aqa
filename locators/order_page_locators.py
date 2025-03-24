from selenium.webdriver.common.by import By


class OrderPageLocators:

    #первая страница формы
    FORM_ORDER_PERSON = (By.XPATH, './/div[text()="Для кого самокат"]')
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    SELECT_METRO_STATION = (By.XPATH, ".//ul/li[5]")
    NUMBER_PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    FORM_NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # вторая страница формы
    FORM_ORDER_RENT = (By.XPATH, './/div[text()="Про аренду"]')
    DELIVERY_DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    MONTH_CALENDAR = (By.XPATH, '//div[contains(@class, "month-container")]')
    SELECTED_DATE = (By.XPATH,
                     "//div[contains(@class, 'react-datepicker__day--selected')]")
    RENT_TIME_FIELD = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    SELECT_RENT_TIME = (By.XPATH, ".//div[@class='Dropdown-option' and text()='трое суток']")
    SELECT_COLOR_SCOOTER = (By.ID, 'black')
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    FORM_ORDER_BUTTON = (
    By.XPATH, '//div[contains(@class, "Order")]/button[text()="Заказать"]')
    # окно подтверждения заказа
    ORDER_CONFIRM = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    BUTTON_CONFIRM = (By.XPATH, ".//button[text()='Да']")
    # окно оформленного заказа
    ORDER_COMPLETED = (By.XPATH, ".//div[text()='Заказ оформлен']")