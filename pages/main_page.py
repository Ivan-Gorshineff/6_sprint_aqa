from allure import step

from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.url = Urls.MAIN_PAGE_URL
    self.locators = MainPageLocators()

  def click_on_question(self, question):
    with step(f'Клик на вопрос {question}'):
      self.scroll_to_element(question)
      self.click_on_element(question)

  def get_answer_text(self, answer):
    with step(f'Текст ответа {answer}'):
      self.wait_for_element_visible(answer)
      text_answer = self.get_text_element(answer)
      return text_answer
