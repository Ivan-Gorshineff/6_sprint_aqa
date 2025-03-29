from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators

class UserData:

    USER_1 = {
        "first_name": 'Иван',
        "last_name": "Ласточкин",
        "address": "Ворошилова, 27",
        "phone_number": "89344555554",
        "delivery_date": "23.05.2025",
        "comment": "Все супер!"
    }

    USER_2 = {
        "first_name": "Антон",
        "last_name": "Пироженко",
        "address": "Шоссейная 43",
        "phone_number": "89486545678",
        "delivery_date": "03.04.2025",
        "comment": "Доставка пришла бысро"
    }

    LIST_DATA_USERS = [
        (BasePageLocators.HEADER_ORDER_BUTTON, USER_1),
        (MainPageLocators.ORDER_BUTTON, USER_2),
    ]