from allure import step
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
import urls


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.Urls.ORDER_PAGE_URL
        self.locators_order_page = OrderPageLocators()
        self.locators_base_page = BasePageLocators()

    def wait_form_order_person(self):
        self.wait_for_element_visible(self.locators_order_page.FORM_ORDER_PERSON)

    def wait_form_order_rent(self):
        self.wait_for_element_visible(self.locators_order_page.FORM_ORDER_RENT)

    def wait_for_element_invisible(self, locator):
        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))

    def enter_text_form_order_person(self, user_data):
        with step(f'Заполнение первой формы'):
            self.wait_form_order_person()
            self.enter_text(self.locators_order_page.FIRST_NAME_FIELD, user_data['first_name'])
            self.enter_text(self.locators_order_page.LAST_NAME_FIELD, user_data['last_name'])
            self.enter_text(self.locators_order_page.ADDRESS_FIELD, user_data['address'])
            self.click_on_element(self.locators_order_page.METRO_STATION_FIELD)
            self.click_on_element(self.locators_order_page.SELECT_METRO_STATION)
            self.enter_text(self.locators_order_page.NUMBER_PHONE_FIELD, user_data['phone_number'])

    def click_on_form_next_button(self):
        with step(f'Клик по кнопке "Далее"'):
            self.click_on_element(self.locators_order_page.FORM_NEXT_BUTTON)

    def enter_text_form_order_rent(self, user_data):
        with step(f'Заполнение второй формы'):
            self.wait_form_order_rent()
            self.enter_text(self.locators_order_page.DELIVERY_DATE_FIELD, user_data['delivery_date'])
            self.click_on_element(self.locators_order_page.FORM_ORDER_RENT)
            self.wait_for_element_invisible(self.locators_order_page.MONTH_CALENDAR)
            self.click_on_element(self.locators_order_page.RENT_TIME_FIELD)
            self.click_on_element(self.locators_order_page.SELECT_RENT_TIME)
            self.click_on_element(self.locators_order_page.SELECT_COLOR_SCOOTER)
            self.enter_text(self.locators_order_page.COMMENT_FIELD, user_data['comment'])

    def click_form_order_button(self):
        with step(f'Клик на кнопку "Заказать"'):
            self.click_on_element(self.locators_order_page.FORM_ORDER_BUTTON)

    def order_confirm(self):
        with step(f'Подтверждение заказа в модальном окне'):
            self.wait_for_element_visible(self.locators_order_page.ORDER_CONFIRM)
            self.click_on_element(self.locators_order_page.BUTTON_CONFIRM)

    def order_status_success(self):
        with step(f'Статус "Зкакз оформлен"'):
            self.wait_for_element_visible(self.locators_order_page.ORDER_COMPLETED)
            return self.get_text_element(self.locators_order_page.ORDER_COMPLETED)

    def click_on_yandex_logo(self):
        with step(f'Click on yandex logo'):
            self.click_on_element(self.locators_base_page.YANDEX_LOGO_BUTTON)

    def click_on_scooter_logo(self):
        with step(f'Click on scooter logo'):
            self.click_on_element(self.locators_base_page.SCOOTER_LOGO_BUTTON)

