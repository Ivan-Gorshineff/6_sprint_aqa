from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from faker import Faker


class UserData:
    fake = Faker()

    USER_1 = {
        "first_name": fake.name(),
        "last_name": fake.last_name(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "rental_date": "23.05.2025",
        "comment": fake.text(10)
    }

    USER_2 = {
        "first_name": fake.name(),
        "last_name": fake.last_name(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "rental_date": "03.04.2025",
        "comment": fake.text(20)
    }

    DATA_ORDER = [
        (BasePageLocators.HEADER_ORDER_BUTTON, USER_1),
        (MainPageLocators.ORDER_BUTTON, USER_2),
    ]