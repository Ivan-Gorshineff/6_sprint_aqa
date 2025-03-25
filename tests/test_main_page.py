import allure
import  pytest


from conftest import driver
from data import DataAccordion
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestAccordion:

    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', DataAccordion.DATA_ACCORDION)
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @allure.description('На странице проверяем, что при клике на каждый вопрос отображается соответсвующий ответ')
    def test_click_accordion_questions(self, driver, question_locator, answer_locator, expected_text):
        page = MainPage(driver)
        page.open()
        page.wait_for_element_visible(MainPageLocators.ACCORDION_LIST)
        page.scroll_to_element(MainPageLocators.ACCORDION_LIST)
        page.click_on_question(question_locator)
        actual_text = page.get_answer_text(answer_locator)
        with allure.step(f"Проверка, что текст ответа '{actual_text}' соответствует ожидаемому '{expected_text}'"):
            assert actual_text == expected_text, f'Ожидалось {expected_text}, но получили {actual_text}'




