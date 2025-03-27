import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import Urls
from pages.order_page import OrderPage
from conftest import driver
from locators.base_page_locators import BasePageLocators


class TestLogoNavigation:

    @allure.title('Клик на логотип "Самокат"')
    @allure.description('При клике на логотип "Самокат" происходит переход на главную страницу')
    def test_click_on_scooter_logo(self, driver):
        page = OrderPage(driver)
        page.open()
        page.wait_for_element_visible(BasePageLocators.SCOOTER_LOGO_BUTTON)
        page.click_on_scooter_logo()
        current_url = page.get_current_url()
        with allure.step(f'Проверяем, что текущая страница {current_url} равна главной странице {Urls.MAIN_PAGE_URL}'):
            assert current_url == Urls.MAIN_PAGE_URL, f'Ожидалось, главная страница это {Urls.MAIN_PAGE_URL}, но получили {current_url}'


    @allure.title('Клик на логотип "Яндекс"')
    @allure.description('При клике на логотип "Яндекс" промсходит переход на страницу Дзен')
    def test_click_on_yandex_logo(self, driver, timeout=30):
        page = OrderPage(driver)
        page.open()
        page.wait_for_element_visible(BasePageLocators.YANDEX_LOGO_BUTTON)
        page.click_on_yandex_logo()
        WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(2))  # ожидаем появления нового окна
        driver.switch_to.window(driver.window_handles[1]) # переключаемся на второе окно
        WebDriverWait(driver, timeout).until(EC.url_contains(Urls.DZEN_YANDEX)) # ожидаем, что ссылка содержит указанный локатор
        current_url = page.get_current_url()
        with allure.step(f'Проверяем, что текущая страница {current_url} равна странице Дзен {Urls.DZEN_YANDEX}'):
            assert current_url == Urls.DZEN_YANDEX, f'Ожидалось, страница Дзен это {Urls.DZEN_YANDEX}, но получили {current_url}'