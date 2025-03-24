from allure import step

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = None

    def open(self,url):
        with step(f'Go to {url}'):
            self.driver.get(url)

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def enter_text(self, locator, text):
        with step(f'Enter text {text} into field with locator {locator}'):
            self.wait_for_element_visible(locator)
            self.driver.find_element(*locator).send_keys(text)

    def click_on_element(self, locator):
        with step(f'Click to {locator}'):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_to_element(self, locator):
        with step(f'Scroll to {locator}'):
            element = self.driver.find_element(*locator)
            self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def current_url(self):
        return self.driver.current_url

    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

