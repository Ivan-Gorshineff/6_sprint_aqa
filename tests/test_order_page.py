import allure
import pytest

from user_data import UserData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver
from locators.base_page_locators import BasePageLocators


class TestOrderScooter:

        @allure.title('Оформление заказа самоката')
        @allure.description('Сценарий оформления заказа двумя пользователями через разные кнопки "Заказать"')
        @pytest.mark.parametrize('order_button, user', UserData.LIST_DATA_USERS)
        def test_order_scooter(self, driver, order_button, user):
            page = MainPage(driver)
            page.open()
            page.wait_for_element_visible(BasePageLocators.SCOOTER_LOGO_BUTTON)
            page.click_order_button(order_button)
            order_page = OrderPage(driver)
            order_page.enter_text_form_order_person(user)
            order_page.click_on_form_next_button()
            order_page.enter_text_form_order_rent(user)
            order_page.click_form_order_button()
            order_page.order_confirm()
            success_order_status_text = order_page.order_status_success()
            with allure.step(f'Проверяем, что "Заказ оформлен" отображается как {success_order_status_text}'):
                assert 'Заказ оформлен' in success_order_status_text, (f'Ожидалось, что текст "Заказ оформлен",'
                                                                       f' но получили {success_order_status_text}')

